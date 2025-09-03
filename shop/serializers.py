from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    about = serializers.CharField()
    categor = serializers.CharField()
    price = serializers.IntegerField()
    off = serializers.IntegerField()
    
class UserSerializer(serializers.Serializer):
    username =  serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=25)
    # role = serializers.CharField(max_length=25)
