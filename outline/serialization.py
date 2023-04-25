from rest_framework.serializers import ModelSerializer
from .models import Link, Server


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'
