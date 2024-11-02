# Generated by Django 5.1.2 on 2024-10-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0008_rename_iamgem_imagem_rename_iamgem_produtos_imagem"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemsPedido",
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
                ("qtd", models.FloatField(default=1)),
                ("preco", models.FloatField()),
                (
                    "produto",
                    models.ManyToManyField(
                        related_name="produto", to="vendas.produtos"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
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
                ("total", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="itemspedido", to="vendas.itemspedido"
                    ),
                ),
            ],
        ),
    ]