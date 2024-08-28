from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SymptomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        symptoms = data['symptoms']

        # Logic to check symptoms and find diseases
        # ...

        await self.send(text_data=json.dumps({
            'diseases': 'diseases'
        }))
