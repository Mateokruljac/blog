# Generated by Django 3.2.11 on 2022-06-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0025_alter_profile_profile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_images',
            field=models.ImageField(blank=True, default='static/images/user.png', null=True, upload_to='images/profile'),
        ),
    ]
