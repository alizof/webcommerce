# Generated by Django 5.1.2 on 2024-10-17 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0009_itemspedido_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemspedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='items',
        ),
        migrations.AddField(
            model_name='itemspedido',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendas.produtos'),
        ),
        migrations.AddField(
            model_name='itemspedido',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendas.pedido'),
        ),
    ]
