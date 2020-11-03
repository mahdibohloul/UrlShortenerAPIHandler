from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import api_shortener_detail, api_post_shortener_url, ApiUrlListView, api_url_direction

urlpatterns = [
    path('<slug>/', api_shortener_detail, name="detail_api"),
    path('create', api_post_shortener_url, name='create_api'),
    path('list', ApiUrlListView.as_view(), name='list_api'),
    path('direction/<slug:key>/', api_url_direction, name='direction_api'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
