import json
import re
from logging import Logger

import websocket

import config
from core import pastebin


class CQBot(websocket.WebSocketApp):
    def __init__(self):
        url = 'ws://{}:{}/'.format(config.WS_ADDRESS, config.WS_PORT)
        self.logger = Logger('CQBot')
        super().__init__(url, on_message=self.__on_message)

    def __on_group_message(self, message: str, message_id: int, group_id: int, sender_nickname: str):
        print('Received group message from {}: {}'.format(sender_nickname, message))
        self.logger.info('Received group message from {}: {}'.format(sender_nickname, message))
        if self.__should_trigger(message):
            print('Triggered, deleting message and pasting it to pastebin.com')
            pb_url = pastebin.create_paste(message, config.PASTEBIN_TITLE_FORMAT.format(sender=sender_nickname))
            data = {
                'action': 'send_group_msg',
                'params': {
                    'group_id': group_id,
                    'message': config.REPLY_FORMAT.format(sender=sender_nickname, pb_url=pb_url),
                }
            }
            self.send(json.dumps(data))
            data = {
                'action': 'delete_msg',
                'params': {
                    'message_id': message_id
                }
            }
            self.send(json.dumps(data))

    def __on_message(self, _, message: str):
        try:
            data = json.loads(message)
            if data['post_type'] == 'message' and data['message_type'] == 'group':
                message = data['message']
                message_id = data['message_id']
                group_id = data['group_id']
                self.__on_group_message(message, message_id, group_id, data['sender']['nickname'])
        except Exception as e:
            self.logger.error('Failed to parse message from CQHttp: {}'.format(e))

    @staticmethod
    def __should_trigger(message: str) -> bool:
        for pattern in config.MATCH_WHITE_LIST:
            if re.match(pattern, message) is not None:
                return False
        if len(message) >= config.TRIGGER_LENGTH:
            return True
        for pattern in config.MATCH_BLACK_LIST:
            if re.match(pattern, message) is not None:
                return True
