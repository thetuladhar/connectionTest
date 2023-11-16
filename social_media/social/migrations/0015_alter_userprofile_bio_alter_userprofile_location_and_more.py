# Generated by Django 4.2.6 on 2023-11-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0014_alter_userprofile_bio_alter_userprofile_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile", name="bio", field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="location",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="images/profile_pictures/default.png",
                null=True,
                upload_to="profile_pics/",
            ),
        ),
    ]
