# Generated by Django 5.1.2 on 2024-12-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_landingbanners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingbanners',
            name='image',
            field=models.ImageField(upload_to='landing_banners/'),
        ),
    ]
