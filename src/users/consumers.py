import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Users
from django.template.loader import render_to_string
from django.core import serializers


class UserConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("users", self.channel_name)
		await self.send_status()

	async def disconnect(self, code):
		await self.channel_layer.group_discard("users", self.channel_name)
		await self.send_status()

	async def send_status(self):
		users = Users.objects.all()
		# users = serializers.serialize('json', users)
		html = render_to_string("includes/list_user.html", {'users': users})
		print(html)
		await self.channel_layer.group_send(
			'users',
			{
				"type": "user_update",
				"event": "Change Status",
				"html_users": html
			}
		)

	async def user_update(self, event):
		await self.send_json(event)
		print('user_update', event)
