# Generated by Django 4.0.6 on 2022-07-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_post_audio_alter_post_file_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]