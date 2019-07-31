from .models import brands
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.dispatch import receiver
from django.template.loader import render_to_string


class BrandsConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("brands", self.channel_name)
        await self.get_new_brand()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("brands", self.channel_name)
        await self.get_new_brand()

    async def get_new_brand(self):
        data = brands.objects.filter(is_deleted=0).order_by('brand_name')
        html = render_to_string('brands/list.html', {'brand_data': data})
        await self.channel_layer.group_send(
            "brands", {"type": "send_brand",
                       "event": "Change brand",
                       "brand": html})

    async def send_brand(self, event):
        await self.send_json(event)
