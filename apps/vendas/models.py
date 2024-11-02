from django.db import models

from apps.authenticator.models import CustomUser

from django.conf import settings
# Create your models here.


class Imagem(models.Model):
  code         = models.CharField(blank=True, null=True, max_length=200, default='')
  file         = models.ImageField(upload_to='image/')
  content_type = models.CharField(max_length=20,null=False, blank=False, default='')

class Produtos(models.Model):
  nome         = models.CharField(max_length=100, null=False, blank=False)
  descricao    = models.CharField(max_length=2000, null=False, blank=False)
  imagem       = models.CharField(max_length=2000, null=True, blank=True, default='')
  preco        = models.FloatField(blank=False,null=False)
  unidade      = models.CharField(max_length=3, null=False, default='UND')
  estoque      = models.FloatField(default=0)
  
CustomUser = settings.AUTH_USER_MODEL
class PedidoVenda(models.Model):
  
  cliente_venda = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cliente', blank=True, null=True)
  valor_total   = models.DecimalField(default=0, decimal_places=2, max_digits=10)
  created_at    = models.DateTimeField(auto_now=True)


class ItensPedidoVenda(models.Model):
  item_venda    = models.CharField(default='0000',max_length=4)
  pedido_venda  = models.ForeignKey(PedidoVenda, on_delete=models.CASCADE, related_name='items', default=0)
  produto_venda = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name='produto', default=0)
  qtd_venda     = models.FloatField(default=1)
  total         = models.DecimalField(default=0, decimal_places=2, max_digits=10)