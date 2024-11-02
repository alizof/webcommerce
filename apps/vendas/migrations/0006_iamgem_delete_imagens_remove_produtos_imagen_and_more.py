# Generated by Django 5.1.2 on 2024-10-15 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0005_imagens_imagen"),
    ]

    operations = [
        migrations.CreateModel(
            name="Iamgem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=200)),
                ("file", models.ImageField(default="", upload_to="image/")),
                ("content_type", models.CharField(default="", max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Imagens",
        ),
        migrations.RemoveField(
            model_name="produtos",
            name="imagen",
        ),
        migrations.AddField(
            model_name="produtos",
            name="iamgem",
            field=models.CharField(blank=True, default="", max_length=2000, null=True),
        ),
    ]
