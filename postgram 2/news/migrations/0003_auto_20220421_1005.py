# Generated by Django 2.1.5 on 2022-04-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220418_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
