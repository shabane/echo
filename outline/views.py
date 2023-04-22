from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Link, Server
from .serialization import LinkSerializer, ServerSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
