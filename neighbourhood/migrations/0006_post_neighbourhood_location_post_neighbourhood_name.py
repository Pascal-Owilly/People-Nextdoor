# Generated by Django 4.0.4 on 2022-04-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0005_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighbourhood_location',
            field=models.CharField(default='location', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='neighbourhood_name',
            field=models.CharField(default='nickname', max_length=100),
        ),
    ]