from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .models import CustomUser

from .serializers import CustomUserSerializer, SignUpUserSerializer

from utils.views_pagination import Pagination
from utils.poui_wies_set import PouiWiesSet, PouiCreateAPIView

from rest_framework import generics
from rest_framework.permissions import AllowAny

from utils.api_response import api_response

class UserViewSet(PouiWiesSet):
    queryset            = CustomUser.objects.all()
    serializer_class    = CustomUserSerializer
    permission_classes  = [permissions.IsAuthenticated]
    pagination_class    = Pagination.DefaultPagination
    viwer_name          = "Usuário"



class SignUpUserView(PouiCreateAPIView):
    queryset            = CustomUser.objects.all()
    serializer_class    = SignUpUserSerializer
    permission_classes  = [AllowAny] 
    pagination_class    = Pagination.DefaultPagination
    viwer_name          = "Usuário"