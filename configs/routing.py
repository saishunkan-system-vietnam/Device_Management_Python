from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from src.brands.consumers import BrandsConsumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('ws_brand/', BrandsConsumers),
    ])
})