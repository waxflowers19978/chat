from django.shortcuts import render


from .python_file.redis import Redis


# Create your views here.

def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    redis = Redis()
    if request.method == 'POST':
        message_text = request.POST['message_text']
        redis.save_message(room_name, message_text)

    message_list = redis.get_message(room_name)
    params = {
        'message_list': message_list
    }
    return render(request, 'chat/room.html', params)
