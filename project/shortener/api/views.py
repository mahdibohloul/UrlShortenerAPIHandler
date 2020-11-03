from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from shortener.models import URLS
from shortener.api.serializers import ShortenerSerializer
from shortener.views import get_shorter_url


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_shortener_detail(request, slug):
    try:
        url = URLS.objects.filter(init_url__contains=slug)
    except URLS.DoesNotExist:
        response = {
            'url': slug,
            'msg': 'Not found'
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    items = {}
    for obj in url:
        items[obj.id] = ShortenerSerializer(obj).data
    return Response(items, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_post_shortener_url(request):
    init_url = request.data['init_url']
    path = request.data['path']
    generated_url = get_shorter_url(init_url=init_url, path=path)
    if request.user_agent.is_mobile:
        device = 'Phone'
    else:
        device = 'Desktop'
    data = {
        'device': device,
        'browser': request.user_agent.browser.family,
        'init_url': init_url,
        'short_url': generated_url,
        'user': request.user.pk
    }
    try:
        url = URLS.objects.filter(user=request.user, init_url=init_url)
        data = {
            'msg': 'You already have this link',
            url.id: ShortenerSerializer(url).data,
        }
        return Response(data, status=status.HTTP_208_ALREADY_REPORTED)
    except URLS.DoesNotExist:
        serializer = ShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_url_direction(request, *args, **kwargs):
    try:
        print(f'slug: {kwargs}')
        print(f'key: {kwargs["key"]}')
        urls = URLS.objects.filter(short_url__contains=kwargs['key'])
    except URLS.DoesNotExist:
        response = {
            'url': kwargs['key'],
            'msg': 'Not found'
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    items = {}
    for obj in urls:
        items[obj.id] = obj.get_absolute_url()
    return Response(items, status=status.HTTP_200_OK)


class ApiUrlListView(ListAPIView):
    queryset = URLS.objects.all()
    serializer_class = ShortenerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_filter = ('init_url', 'short_url', 'device', 'browser')
