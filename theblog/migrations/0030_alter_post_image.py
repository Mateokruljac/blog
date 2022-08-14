# Generated by Django 3.2.11 on 2022-08-14 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0029_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
