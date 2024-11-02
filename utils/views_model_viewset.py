from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .api_response import api_response 

class PouiViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            
            serializerQuery = self.get_serializer(queryset, many=True)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                paginator = self.paginator.get_paginated_response(serializer).data
                
                return api_response.poui_response(serializer.data, bool(paginator['next']), paginator)
            
            return api_response.poui_response(serializerQuery.data, (self.paginator.page_size < len(serializerQuery.data)))
        
        except ValidationError as e:
            return api_response.poui_erro_msg_response(e)
        except Exception as e:
            return api_response.poui_msg_simple_response(
                401, 'error', str(e), '', status.HTTP_400_BAD_REQUEST
            )
            
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
                        
            return api_response.poui_simple_response(
                        serializer.data,
                        [api_response.poui_default_msg(
                            200, 'success', 
                            f'{self.viwer_name} criado com sucesso!'
                        )]
                    )
        except ValidationError as e:
            return api_response.poui_erro_msg_response(e)
        except Exception as e:
            return api_response.poui_msg_simple_response(
                401, 'error', str(e), '', status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):

        try:
            partial = kwargs.pop('partial', True)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return api_response.poui_simple_response(
                serializer.data,
                [api_response.poui_default_msg(
                    200, 'success', 
                    f'{self.viwer_name} atualizado com sucesso.'
                )]
            )
        except ValidationError as e:
            return api_response.poui_erro_msg_response(e)
        except Exception as e:
            return api_response.poui_msg_simple_response(
                401, 'error', str(e), '', status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            self.perform_destroy(instance)
            
            return api_response.poui_simple_response(
                True,
                [api_response.poui_default_msg(
                    200, 'success', 
                    f'{self.viwer_name} removido com sucesso.'
                )]
            )
        except ValidationError as e:    
            return api_response.poui_erro_msg_response(e)
        except Exception as e:
            return api_response.poui_msg_simple_response(
                401, 'error', str(e), '', status.HTTP_400_BAD_REQUEST
            )
    
    
    
