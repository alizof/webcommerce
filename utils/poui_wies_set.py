from rest_framework import viewsets
from rest_framework import status
from rest_framework.exceptions import ValidationError

from rest_framework import generics

from utils.api_response import api_response

class PouiWiesSet(viewsets.ModelViewSet):
  def list(self, request):
    try:
     
      filter_backends = self.filter_backends
      queryset = self.filter_queryset(self.get_queryset())
      

      for backend in filter_backends:
        queryset = backend().filter_queryset(request, queryset, self)
        
      page = self.paginate_queryset(queryset)
      
      serializer_query = self.get_serializer(queryset, many=True)
      
      if page is not None:
        serializer = self.get_serializer(page, many=True)
        paginator = self.paginator.get_paginated_response(serializer).data
        
        return api_response.poui_response(serializer.data, bool(paginator['next']), paginator)
      
      return api_response.poui_response(serializer_query.data, self.paginator.page_size < len(serializer_query.data))
    except Exception as e:
      return api_response.poui_msg_simple_response(401, 'error', str(e), status.HTTP_400_BAD_REQUEST)
  
  def create(self, request, *args, **kwargs):
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      
      
      return api_response.poui_simple_response(serializer.data, [api_response.poui_default_msg(200, 'success', f'{self.viwer_name} - Criado com sucesso!')])
    except ValidationError as e:
      return api_response.poui_erro_msg_response(e)
    
    except Exception as e:
      return api_response.poui_msg_simple_response(400,status.HTTP_400_BAD_REQUEST,'error', str(e))
    
  def update(self, request, *args, **kwargs):
    try:
      partial = kwargs.pop('partial', True)
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data, partial=partial)
      serializer.is_valid(raise_exception=True)
      self.perform_update(serializer)
      
      return api_response.poui_simple_response(serializer.data, [api_response.poui_default_msg(200, 'success', f'{self.viwer_name} - Atualizado com sucesso!')])
    
    except ValidationError as e:
      return api_response.poui_erro_msg_response(e)
    
    except Exception as e:
      return api_response.poui_msg_simple_response(400,status.HTTP_400_BAD_REQUEST,'error', str(e))
    
  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data)
      self.perform_destroy(instance)
      
      return api_response.poui_simple_response(True, [api_response.poui_default_msg(200,'success', f'{self.viwer_name} - Removida com sucesso!')])
    
    except ValidationError as e:
      return api_response.poui_erro_msg_response(e)
    
    except Exception as e:
      return api_response.poui_msg_simple_response(400,status.HTTP_400_BAD_REQUEST,'error', str(e))
    

class PouiCreateAPIView(generics.ListCreateAPIView):
  def create(self, request, *args, **kwargs):
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      
      
      return api_response.poui_simple_response(serializer.data, [api_response.poui_default_msg(200, 'success', f'{self.viwer_name} - Criado com sucesso!')])
    except ValidationError as e:
      return api_response.poui_erro_msg_response(e)
    
    except Exception as e:
      return api_response.poui_msg_simple_response(400,status.HTTP_400_BAD_REQUEST,'error', str(e))
  
  def list(self, request):
    try:
     
      filter_backends = self.filter_backends
      queryset = self.filter_queryset(self.get_queryset())
      

      for backend in filter_backends:
        queryset = backend().filter_queryset(request, queryset, self)
        
      page = self.paginate_queryset(queryset)
      
      serializer_query = self.get_serializer(queryset, many=True)
      
      if page is not None:
        serializer = self.get_serializer(page, many=True)
        paginator = self.paginator.get_paginated_response(serializer).data
        
        return api_response.poui_response(serializer.data, bool(paginator['next']), paginator)
      
      return api_response.poui_response(serializer_query.data, self.paginator.page_size < len(serializer_query.data))
    except Exception as e:
      return api_response.poui_msg_simple_response(401, 'error', str(e), status.HTTP_400_BAD_REQUEST)