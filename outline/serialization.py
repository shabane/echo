from rest_framework.serializers import ModelSerializer
from .models import Link, Server


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['name', 'max_size', 'enabled', 'exp_date', 'note', 'server']


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'
        


class LinkSerializerReadonly(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
