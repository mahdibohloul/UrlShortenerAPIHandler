from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully registered a new user.'
        data['email'] = user.email
        data['username'] = user.username
        token = Token.objects.get(user=user).key
        data['toke'] = token
    else:
        data = serializer.errors
    return Response(data=data)

