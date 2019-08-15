
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
        message_list = self.conn.lrange(room_name, 0, -1)
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
        user_id = room_name.split('_')[0]
        key = self.decide_save_key(room_name)
        dt_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        message = user_id + '.' + dt_now + '.' + message_text
        self.conn.lpush(key, message)
        return

    """
    redis key rule
    -> 'minimumUserId_maximumUserId'
    """
    def decide_save_key(self, room_name):
        num_1, num_2 = room_name.split('_')#<- 顔みたいになってる
        if num_1 < num_2:
            minimumUserId = num_1
            maximumUserId = num_2
        else:
            minimumUserId = num_2
            maximumUserId = num_1
        key = '{}_{}'.format(minimumUserId, maximumUserId)
        return key
