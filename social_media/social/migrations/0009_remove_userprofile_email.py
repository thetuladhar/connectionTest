# Generated by Django 4.2.6 on 2023-11-13 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0008_userprofile_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="email",),
    ]
