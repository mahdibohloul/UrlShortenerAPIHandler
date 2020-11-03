# Generated by Django 3.1.2 on 2020-11-02 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='original_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='urls',
            name='retrieve_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
