from rest_framework import serializers
from shortener.models import URLS

import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=1)


class ShortenerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_user')

    class Meta:
        model = URLS
        fields = ['user', 'username', 'init_url', 'short_url', 'device', 'browser', 'retrieve_time']

    def get_username_from_user(self, url):
        username = url.user.username
        return username



