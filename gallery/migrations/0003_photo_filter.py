# Generated by Django 2.2.3 on 2019-07-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190717_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='filter',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
