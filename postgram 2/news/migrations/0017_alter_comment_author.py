# Generated by Django 4.0.6 on 2022-07-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
