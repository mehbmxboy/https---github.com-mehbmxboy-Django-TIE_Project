# Generated by Django 3.2.7 on 2021-09-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0015_testoo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
