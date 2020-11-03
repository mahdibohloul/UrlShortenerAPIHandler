from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shortener-home'),
    path('shortener/', views.shortener_urls, name='shortener-urls'),
    path('shortener/redirections/', views.urls_list, name='redirections-urls'),
    path('shortener/filter/', views.urls_filter, name='filter-urls'),
]