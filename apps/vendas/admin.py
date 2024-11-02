from django.contrib import admin

from .models import Produtos, Imagem, PedidoVenda, ItensPedidoVenda
# Register your models here.

admin.site.register(Produtos)
admin.site.register(Imagem)
admin.site.register(PedidoVenda)
admin.site.register(ItensPedidoVenda)
