# Generated by Django 5.0.3 on 2024-08-09 03:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0012_auto_20240808_1407"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
    ]