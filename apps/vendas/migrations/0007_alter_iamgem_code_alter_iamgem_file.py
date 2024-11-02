# Generated by Django 5.1.2 on 2024-10-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0006_iamgem_delete_imagens_remove_produtos_imagen_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="iamgem",
            name="code",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="iamgem",
            name="file",
            field=models.ImageField(upload_to="image/"),
        ),
    ]
