# Generated by Django 5.1.2 on 2024-10-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticator", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="phone_number",
        ),
        migrations.AddField(
            model_name="customuser",
            name="cgc",
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
