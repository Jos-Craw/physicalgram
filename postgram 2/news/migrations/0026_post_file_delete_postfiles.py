# Generated by Django 4.0.6 on 2022-08-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0025_remove_post_file_postfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='PostFiles',
        ),
    ]