# Generated by Django 5.0.3 on 2024-07-31 01:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_rename_short_into_to_short_intro"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="short_into",
            new_name="short_intro",
        ),
    ]
