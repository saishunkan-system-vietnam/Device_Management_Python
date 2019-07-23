from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from src.brands.consumers import BrandsConsumers
from src.users.consumers import UserConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('ws_brand/', BrandsConsumers),
        path('ws_user/', UserConsumer)
    ])
})
