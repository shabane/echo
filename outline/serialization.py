from rest_framework.serializers import ModelSerializer
from .models import Link, Server


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'max_size', 'usage', 'enabled', 'key', 'exp_date']


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = ['apiUrl', 'certSha256']
