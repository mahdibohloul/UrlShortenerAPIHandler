from django.db import models
from django.contrib.auth.models import User


class URLS(models.Model):
    user = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE)
    init_url = models.URLField()
    short_url = models.URLField()
    DEVICES = (('Phone', 'Phone'), ('Desktop', 'Desktop'))
    device = models.CharField(max_length=20, choices=DEVICES)
    browser = models.CharField(max_length=20)
    retrieve_time = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return f'{self.init_url}'



