# Generated by Django 4.0.6 on 2022-07-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_advuser_first_name_alter_advuser_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='file',
        ),
    ]
