from django.shortcuts import render, redirect
from django.conf import settings
import redis
from .forms import ShortenerForms
from .models import URLS
from .filters import URLFilter
import uuid
from datetime import timedelta, datetime

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=2)


def home(request):
    return render(request, 'shortener/home.html', {'title': 'Home'})


def get_shorter_url(init_url, path):
    first_url = init_url
    http_code = first_url[:first_url.index('/')]
    site_name = ''.join(first_url[first_url.index('/') + 2:])
    try:
        site_name = site_name[:site_name.index('/')]
    except:
        pass
    second_url = f'{http_code}//{str(uuid.uuid4())}.{site_name}/'
    if path:
        second_url = second_url + path
    return second_url


def shortener_urls(request):
    form = ShortenerForms(request.POST or None)
    if form.is_valid():
        generated_url = get_shorter_url(init_url=form.cleaned_data['init_url'], path=form.cleaned_data['path'])
        try:
            URLS.objects.get(user__exact=request.user, init_url__exact=form.cleaned_data['init_url'])
            return redirect('shortener-urls')
        except URLS.DoesNotExist:
            redis_instance.set(generated_url, form.cleaned_data['init_url'])
            create_url_reporting(request, init_url=form.cleaned_data['init_url'], generated_url=generated_url)
            return redirect('shortener-urls')
    context = {
        'form': form
    }
    return render(request, 'shortener/shortener_urls.html', context=context)


def create_url_reporting(request, init_url, generated_url):
    if request.user_agent.is_mobile:
        device = 'Phone'
    else:
        device = 'Desktop'
    browser = request.user_agent.browser.family
    URLS.objects.create(user=request.user, init_url=init_url, short_url=generated_url,
                        device=device, browser=browser)


def urls_list(request):
    objects = URLS.objects.filter(user=request.user)
    return render(request, "shortener/redirections_urls.html", {"objects": objects})


# def get_sql_raw_code(date, device, browser):
#     date_condition = 0
#     if date == 'Today':
#         date_condition = datetime.today() - timedelta(days=1)
#     elif date == 'Previous Week':
#         date_condition = datetime.today() - timedelta(weeks=1)
#     elif date == 'Previous Month':
#         date_condition = datetime.today() - timedelta(days=30)
#     raw_sql_code = """select * from shortener_urls where browser=['browser'] and device="'+device+'" and
#     retrieve_time between "'+date_condition+'" and now()"""
#
#     return raw_sql_code


def urls_filter(request):
    urls = URLS.objects.all()
    my_filter = URLFilter(request.GET, queryset=urls)
    urls = my_filter.qs
    context = {
        'filters': my_filter,
        'objects': urls
    }
    return render(request, 'shortener/filter_urls.html', context)
