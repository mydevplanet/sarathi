# Generated by Django 5.0 on 2024-01-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_volunteer_vol_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='vol_image',
            field=models.ImageField(upload_to='volunteer/'),
        ),
    ]
