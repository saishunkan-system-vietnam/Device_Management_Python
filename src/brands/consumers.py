from .models import brands
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.http import HttpResponse


class BrandsConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("brands", self.channel_name)
        await self.get_new_brand()        

    async def disconnect(self):
        await self.channel_layer.group_discard("brands", self.channel_name)

    async def get_new_brand(self):
        data = brands.objects.filter(is_deleted=0).order_by('brand_name')
        html = render_to_string('brands/list.html', {'brand_data': data})
        await self.channel_layer.group_send(
            "brands", {"type": "send_brand",
                       "event": "Change brand",
                       "brand": html})

    async def send_brand(self, event):
        await self.send_json(event)


class BrandsChartConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("brands_chart", self.channel_name)
        await self.get_new_chart_brand()

    async def disconnect(self):
        await self.channel_layer.group_discard("brands_chart", self.channel_name)

    async def get_new_chart_brand(self):
        data = brands.objects.raw(
            'SELECT COUNT(id) as id, MONTH(created_time) as created_month FROM brands GROUP BY MONTH(created_time)')
        arr_data = []
        for x in range(12):
            quantity = 0
            for val in data:
                if(val.created_month == (x+1)):
                    quantity = val.id
            arr_data.append({'month': (x+1), 'quantity': quantity})
        html = render_to_string('brands/paintchart.html',
                                {'data_chart': arr_data})
        print(html)
        await self.channel_layer.group_send(
            "brands_chart", {"type": "send_brand_chart",
                             "event": "Change brand chart",
                             "chart": html})
                            

    async def send_brand_chart(self, event):
        await self.send_json(event)
