# Generated by Django 3.0.7 on 2020-06-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20200610_1550'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]