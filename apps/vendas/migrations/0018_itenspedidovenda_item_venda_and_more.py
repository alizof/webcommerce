# Generated by Django 5.1.2 on 2024-10-17 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0017_alter_itenspedidovenda_pedido_venda"),
    ]

    operations = [
        migrations.AddField(
            model_name="itenspedidovenda",
            name="item_venda",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="itenspedidovenda",
            name="produto_venda",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="produto",
                to="vendas.produtos",
            ),
        ),
        migrations.AddField(
            model_name="itenspedidovenda",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="itenspedidovenda",
            name="pedido_venda",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="vendas.pedidovenda",
            ),
        ),
        migrations.AlterField(
            model_name="pedidovenda",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]