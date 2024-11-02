import uuid


from rest_framework import serializers

from apps.authenticator.models import CustomUser
from .models import Produtos, Imagem, PedidoVenda, ItensPedidoVenda

class UserSerializer(serializers.ModelSerializer):
  class Meta():
    model  = CustomUser
    fields = '__all__'
    extra_kwargs= {
      'password': {'write_only': True}
    }


class ProdutoSerializer(serializers.ModelSerializer):
  class Meta():
    model   = Produtos
    fields  = '__all__'


class ImagemSerializer(serializers.ModelSerializer):
  class Meta():
    model   = Imagem
    fields  = '__all__'


class ItemSerializer(serializers.ModelSerializer): 
  produto_venda_id = serializers.PrimaryKeyRelatedField(queryset=Produtos.objects.all(), source='produto_venda', write_only=True)
  produto_venda = ProdutoSerializer(read_only=True)

  class Meta:
      model = ItensPedidoVenda
      fields = ['id', 'item_venda', 'qtd_venda', 'produto_venda', 'produto_venda_id'] 


class PedidoVendaSerializer(serializers.ModelSerializer):
  items = ItemSerializer(many=True)
  cliente_venda_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='cliente_venda', write_only=True)
  cliente_venda = UserSerializer(read_only=True)

  class Meta():
    model = PedidoVenda
    fields = ['id', 'cliente_venda','cliente_venda_id','total','items']

  def validate_items(self, validated_data):
    if len(validated_data) <= 0:
      raise serializers.ValidationError('Informe ao menos 1 Item.')
    return validated_data
  
  def create(self, validated_data):
    items_data = validated_data.pop('items', [])
    

    pedido = PedidoVenda.objects.create(**validated_data)

    for item_data in items_data:
      pedido.total += item_data['qtd_venda']
      ItensPedidoVenda.objects.create(pedido_venda=pedido, **item_data)

      
    pedido.save()
    return pedido

  