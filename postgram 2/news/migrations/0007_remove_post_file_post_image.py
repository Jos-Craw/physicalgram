# Generated by Django 4.0.6 on 2022-07-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_image_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]