# Generated by Django 5.1.2 on 2024-10-17 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0016_itenspedidovenda"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenspedidovenda",
            name="pedido_venda",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="vendas.pedidovenda",
            ),
        ),
    ]