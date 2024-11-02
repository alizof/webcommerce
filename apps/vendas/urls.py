from django.urls import include, path
from rest_framework import routers

from .views import ProdutoViewSet, ImagemViweSet, PedidoVendaViewSet


router = routers.DefaultRouter()
router.register(r'produto', ProdutoViewSet, basename='produto')
router.register(r'pedidovenda', PedidoVendaViewSet, basename='pedidovenda')


urlpatterns = [
  path('', include(router.urls)),
  path('imagem', ImagemViweSet.as_view(), name="upload-iamgem"),
  path('imagem/<str:code>', ImagemViweSet.as_view(), name="upload-iamgem"),
]
