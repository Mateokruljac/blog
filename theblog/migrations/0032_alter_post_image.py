# Generated by Django 3.2.11 on 2022-08-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0031_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]