# Generated by Django 3.2.7 on 2021-09-21 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0044_auto_20210919_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likepost',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='like_count',
        ),
    ]
