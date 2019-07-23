from .models import brands
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.core.signals import request_finished
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core import serializers
from django.template.loader import render_to_string

class BrandsConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def brand_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")


@receiver(request_finished)
def my_callback(sender, **kwargs):
    data = brands.objects.filter(is_deleted=0).order_by('brand_name')
    html = render_to_string('brands/list.html', { 'brand_data': data }) 
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {"type": "brand.gossip",
                   "event": "Change brand",
                   "brand": html})    
##############################
# from channels.generic.websocket import WebsocketConsumer
# from .models import brands
# from django.core import serializers

# class BrandsConsumers(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#         print('============connect')
#         data = brands.objects.filter(is_deleted=0).order_by('brand_name')
#         datajson = serializers.serialize('json', list(data))    
#         self.send(datajson)
#         self.close()
#     def close(self, code=None):
#         self.close()
