from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json

class ChatAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        try:
            my_user_id = self.scope['user'].id
            other_user_id = self.scope['url_route']['kwargs']['id']

            # creating group
            if int(my_user_id) < int(other_user_id):
                self.room_name = str(my_user_id) + str(other_user_id)
            else:
                self.room_name = str(other_user_id) + str(my_user_id)
            self.private_chat_room = self.room_name

            #adding channel in group
            await self.channel_layer.group_add(
                self.private_chat_room,
                self.channel_name
            )
        except Exception as e:
            pass

        await self.send({
            'type':'websocket.accept'
        })


    async def websocket_receive(self, event):
        data = json.loads(event['text'])
        if self.scope["user"].is_authenticated:
            
            data['user'] = self.scope['user'].username
            await self.channel_layer.group_send(self.private_chat_room, {
                'type':'chat.message',
                'message':json.dumps(data)
            })
        else:
            await self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"Plese Login First!"})
            })

    async def chat_message(self, event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })


    async def websocket_disconnect(self, event):
        raise StopConsumer()