# Generated by Django 4.0.1 on 2022-01-22 19:19

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]
