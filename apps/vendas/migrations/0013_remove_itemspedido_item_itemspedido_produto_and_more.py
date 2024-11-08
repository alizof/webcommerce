# Generated by Django 5.1.2 on 2024-10-17 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0012_alter_itemspedido_preco"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itemspedido",
            name="item",
        ),
        migrations.AddField(
            model_name="itemspedido",
            name="produto",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="produto",
                to="vendas.produtos",
            ),
        ),
        migrations.AlterField(
            model_name="itemspedido",
            name="pedido",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="vendas.pedido",
            ),
        ),
    ]
