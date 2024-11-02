
from rest_framework import viewsets, permissions
from utils.poui_wies_set import PouiWiesSet, PouiCreateAPIView

from utils.views_pagination import Pagination


from .models import Produtos, PedidoVenda
from .serializers import ProdutoSerializer, ImagemSerializer, PedidoVendaSerializer

from rest_framework import generics

from rest_framework.serializers import Serializer, FileField

from django.db import transaction

# Create your views here.

from unidecode import unidecode

import os
import uuid
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse

from rest_framework.response import Response
from rest_framework import status

class ProdutoViewSet(PouiWiesSet):
  queryset = Produtos.objects.all()
  serializer_class = ProdutoSerializer
  permission_classes = [permissions.IsAuthenticated]
  pagination_class = Pagination.DefaultPagination
  viwer_name = 'Produto'

class PedidoVendaViewSet(PouiWiesSet):
  queryset = PedidoVenda.objects.all()
  serializer_class = PedidoVendaSerializer
  permission_classes = [permissions.IsAuthenticated]
  pagination_class = Pagination.DefaultPagination
  viwer_name = 'Pedido de Venda'



# ---------------------------------------------------
# CUSTOM DJANGO VIWE
class ImagemViweSet(PouiCreateAPIView):

  serializer_class = ImagemSerializer

  def list(self, request, *args, **kwargs):
    code = kwargs.get('code') 

    image_path = os.path.join('image', f'{code}') 

    if not os.path.exists(image_path):
        raise Http404("Imagem não encontrada")

    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

  def post(self, request, *args, **kwargs):
    content_type = request.data['file'].content_type
    code = f"{uuid.uuid4()}-{unidecode(request.data['file'].name).replace(' ', '')}"
    
    request.data['file'].name = code

    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()
        instance.code = code
        instance.content_type = content_type
        instance.save()

        return Response(serializer.data)

    return Response(serializer.errors, status=400)