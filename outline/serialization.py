from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Link, Server, Channel


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'max_size', 'enabled', 'exp_date', 'note', 'server']


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'
        


class LinkSerializerReadonly(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class ChannelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['username', 'name']
