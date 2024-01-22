# Generated by Django 5.0 on 2024-01-22 07:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='base.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
