# Generated by Django 5.1.3 on 2024-11-12 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='mini_description',
        ),
    ]
