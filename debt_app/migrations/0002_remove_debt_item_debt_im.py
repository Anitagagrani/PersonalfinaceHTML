# Generated by Django 3.2.5 on 2021-07-27 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debt_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt_item',
            name='debt_im',
        ),
    ]
