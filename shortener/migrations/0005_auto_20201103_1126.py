# Generated by Django 3.1.2 on 2020-11-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20201103_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='retrieve_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]