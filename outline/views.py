from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Link, Server
from .serialization import LinkSerializer, ServerSerializer, LinkSerializerReadonly, ChannelSerializer
from rest_framework.response import Response
from .core.outline import Outline
from .models import Server, Link, Channel
from .core.pysbin import ubuntuir, headers
from rest_framework import status
from .core import utils
import qrcode
import base64
from rest_framework.views import APIView


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
        
    def create(self, request, *args, **kwargs):
        serializer_class = LinkSerializer(data=request.data)
        if serializer_class.is_valid():
            outline_server = Outline(serializer_class.validated_data['server'].apiUrl)
            __name = serializer_class.validated_data['name']
            __max_usage = serializer_class.validated_data['max_size'] * 1_000_000_000
            __key = outline_server.new_access_key(name=__name, usage_limit=__max_usage)
            __note = serializer_class.validated_data['note']
            __enabled = serializer_class.validated_data['enabled']
            __expire = serializer_class.validated_data['exp_date']
            __server = serializer_class.validated_data['server']

            __domain = serializer_class.validated_data['server'].wrapper_ip
            __port = serializer_class.validated_data['server'].wrapper_port
            __key_url = utils.re_wrapp_domain(__key['accessUrl'], __domain, __port)+f'#{__name}'

            __paste_bin_link = ubuntuir.paste(__key_url)
            
            Link.objects.create(name=__name, max_size=__max_usage, key=__key_url, note=__note, enabled=__enabled, exp_date=__expire, pastebin_link=__paste_bin_link, server=__server, outline_id=__key['id'])

            if __server.channel:
                __channel = Channel.objects.get(pk=__server.channel.id)
                qrcode.make(__key_url).save(f'static/{__name.strip()}.png')
                __qrcode = open(f'static/{__name.strip()}.png', 'rb')
                
                utils.send_to_telegram(
                channel_id=__channel.username,
                caption=f"""
                    \nname: {__name}\n
                    usage: {__max_usage/1_000_000_000} GB\n
                    pastebin: {__paste_bin_link}\n
                    note: {__note}\n
                    server: {__server.name}\n
                    """,
                    img=__qrcode,
                )
                __qrcode.close()
            
            return Response({
                'ok': True,
                'name': __name,
                'max_size': __max_usage,
                'enabled': __enabled,
                'key': __key_url,
                'exp_date': serializer_class.validated_data['exp_date'],
                'paste_bin_link': __paste_bin_link,
                'note': __note,
                'server': __server.name,
                'outline_id': __key['id'],
            })
        return Response({
            'ok': False,
            'message': serializer_class.error_messages,
        })


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        _ = False
        outline_server = Outline(instance.server.apiUrl)
        if(_ := outline_server.delete_key(instance.outline_id)):
            self.perform_destroy(instance)
        return Response({
            'ok': _,
        }, status=status.HTTP_204_NO_CONTENT)

    
    def update(self, request, *args, **kwargs):
        serializer_class = LinkSerializer(data=request.data)
        if serializer_class.is_valid():
            instance = self.get_object()
            outline_server = Outline(instance.server.apiUrl)
            outline_server.set_name(instance.outline_id, serializer_class.validated_data['name'])
            outline_server.set_date_limit(instance.outline_id, serializer_class.validated_data['max_size'] * 1_000_000_000)
            return super().update(request, *args, **kwargs)
        return Response({
                'ok': False,
                'message': serializer_class.error_messages,
            })

class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class LinkViewReadonly(ReadOnlyModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializerReadonly


class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class BatchKeyView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'ok': True  
        })
        
    def post(self, request, *args, **kwargs):
        prefix_name = request.data['prefix_name']
        server = request.data['server']
        size = request.data['size']
        count = request.data['count']
        note = request.data['note']
        exp_date = request.data['exp_date']
        
        if type(size) != int or type(server) != int or type(count) != int:
            return Response({
                'ok': False,
                'message': 'size, server and count should be a postive intiger',
            })
        
        if(_ := Server.objects.get(pk=server)):
            __keys = []
            outline_server = Outline(_.apiUrl)
            __link_count = Link.objects.count()
            for i in range(__link_count+1, __link_count+count+1):
                __key = outline_server.new_access_key(f'{prefix_name}{i}', size*1_000_000_000)
                __key_link = utils.re_wrapp_domain(__key['accessUrl'], _.wrapper_ip, _.wrapper_port)+f'#{prefix_name}{i}'
                __keys.append(__key_link)
                __pastebin = ubuntuir.paste(__key_link)
                Link.objects.create(
                    name = f'{prefix_name}{i}',
                    max_size = size*1_000_000_000,
                    key = __key_link,
                    exp_date = exp_date,
                    pastebin_link = __pastebin,
                    note = note,
                    server = _,
                    outline_id = __key['id'],
                )
                
                if _.channel:
                    qrcode.make(__key_link).save(f'static/{prefix_name}{i}.png')
                    __qrcode = open((f'static/{prefix_name}{i}.png'), 'rb')
                    utils.send_to_telegram(
                        channel_id=_.channel.username,
                        caption=f"""
                        \nname: {f'{prefix_name}{i}'}
                        
                        key: {__key_link}
                        
                        pastebin: {__pastebin}
                        
                        note: {note}
                        
                        server: {_.name}
                        """,
                        img=__qrcode
                        )
                    __qrcode.close()
            return Response({
                'ok': True,
                'keys': __keys,
            })