
import redis as redis_function
import datetime


class Redis():
    """
    connect
    """
    def __init__(self):
        self.conn = redis_function.StrictRedis(host='localhost', port=6379, db=0)
        return

    """
    argumnt -> room_name
    return value -> message_list
    """
    def get_message(self, room_name):
        message_list = self.conn.lrange(room_name, 0, 10)
        message_list = self.decode_message(message_list)
        return message_list

    """
    decode message to "utf-8"
    """
    def decode_message(self, message_list):
        message_list = [message.decode('utf-8') for message in message_list]
        return message_list

    """
    add message to redis
    """
    def save_message(self, room_name, message_text):
        dt_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        message = '0.' + dt_now + '.' + message_text
        self.conn.lpush('0_1', message)
        return
