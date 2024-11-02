from rest_framework import serializers
from .models import CustomUser

from utils.api_response import api_response

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' 
    
    def to_representation(self, instance):
        itens = super().to_representation(instance)
        itens.pop('password')
        
        return itens
    
    
class SignUpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','cgc', 'password']
     
    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])  # Define a senha corretamente
        user.save()
        
        return user
       
    def to_representation(self, instance):
        itens = super().to_representation(instance)
        itens.pop('password')
        
        return itens