from django.shortcuts import render
from django.contrib.auth.models import User


from .python_file.redis import Redis


# Create your views here.
def home(request):
    return render(request, 'chat/home.html')


def index(request):
    # print(request.user)
    # print(type(str(request.user)))
    user_list = User.objects.all().exclude(id=request.user.id)
    # user_list = User.objects.all().exclude(name=request.user.name)
    params = {
        'user_list': user_list,
        # 'my_name': my_name,
    }
    return render(request, 'chat/index.html', params)

def get_key(room_name):
    num_1, num_2 = room_name.split('_')#<- 顔みたいになってる
    if num_1 < num_2:
        minimumUserId = num_1
        maximumUserId = num_2
    else:
        minimumUserId = num_2
        maximumUserId = num_1
    key = '{}_{}'.format(minimumUserId, maximumUserId)
    return key

def room(request, room_name):
    redis = Redis()
    if request.method == 'POST':
        message_text = request.POST['message_text']
        redis.save_message(room_name, message_text)

    my_id, other_id = room_name.split('_')
    other_name = User.objects.all().get(id=other_id)
    key = get_key(room_name)
    message_list = redis.get_message(key)
    params = {
        'message_list': message_list,
        'my_id': my_id,
        'other_name':other_name,
    }
    return render(request, 'chat/room.html', params)

def ajax(request):
    return render(request, 'chat/ajax.html')
