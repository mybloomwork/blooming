# Generated by Django 3.0.9 on 2020-09-27 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='place',
            new_name='state',
        ),
    ]
