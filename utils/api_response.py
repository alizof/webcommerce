from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class api_response():
    
    def poui_erro_msg_response(e:ValidationError):
        for field, errors in e.detail.items():
           return api_response.poui_msg_simple_response(
                400, 
                'warning', 
                f"Erro no campo {field.upper()}",
                [str(error) for error in errors]
            )
        
    def poui_msg_response(msg=[],status=status.HTTP_200_OK):
        # Type - 'error' or 'warning' or 'information'
        data = {
            "_messages": msg
        }
        return Response(data,status=status)
    
    def poui_msg_simple_response(code=400,type='error',message='',detail_message='',status=status.HTTP_400_BAD_REQUEST):
        # Type - 'error' or 'warning' or 'information'
        data = {
            "code": code,
            "type": type,
            "message": message,
            "detailedMessage": detail_message
        }
        return Response(data,status=status)

       
    def poui_response(items=[],hasNext=False,django_rest={},status=status.HTTP_200_OK,msg=[]):
        django = {}
        
        if 'count' in django_rest and django_rest['count']:
            django['count'] = django_rest['count']
        if 'next' in django_rest and django_rest['next']:
            django['next'] = django_rest['next']
        if 'previous' in django_rest and django_rest['previous']:
            django['previous'] = django_rest['previous']
        
        data = {
            "items": items,
            "django_rest": django,
            "hasNext": hasNext,
            "_messages": msg
        }
        
        return Response(data,status=status)
    
    def poui_simple_response(items=any,messages=[]):
        data = {
            "items":items,
            "_messages": messages
        }
        
        return Response(data,status=status.HTTP_200_OK)
    
    def poui_default_msg(code=400,type='error' or 'warning' or 'information' or 'success',message='',detail_message=''):
        # Type - 'error' or 'warning' or 'information' or 'success
        return {
            "code": code,
            "type": type,
            "message": message,
            "detailedMessage": detail_message
        }
    