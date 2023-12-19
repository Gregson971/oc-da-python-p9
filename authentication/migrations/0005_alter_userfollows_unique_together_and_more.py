# Generated by Django 4.2.7 on 2023-12-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0004_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userfollows",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="userfollows",
            constraint=models.UniqueConstraint(
                fields=("user", "followed_user"), name="unique_follow"
            ),
        ),
    ]
