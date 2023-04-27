from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Link, Server
from .serialization import LinkSerializer, ServerSerializer
from rest_framework.response import Response
from .core.outline import Outline
from .models import Server, Link


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
        
    def create(self, request, *args, **kwargs):
        serializer_class = LinkSerializer(data=request.data)
        if serializer_class.is_valid():
            # outline_server = Outline(Server.objects.get())
            # OrderedDict([('name', 'the test'), ('max_size', 555), ('usage', 7777), ('enabled', True), ('key', 'the key'), ('exp_date', datetime.date(2023, 4, 27)), ('pastebin_link', 'lsjfl'), ('note', 'lksdjflsjdf'), ('server', <Server: me and mehdi>)])
            #TODO: 1. get the server and crate its Outline instance
            #TODO: 2. add the new user to outline server
            #TODO: 3. append the data to user table in database
            print(serializer_class.validated_data)
        return Response(request.data)


class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
