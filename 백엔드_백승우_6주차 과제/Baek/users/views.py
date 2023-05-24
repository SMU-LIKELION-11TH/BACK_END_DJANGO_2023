from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.models import User
def users_view(request):
    user1 = User.objects.get(id=1)

    context = {
        'user1': user1
    }

    return render(request, 'temp_users.html', context)

def login_view(request):
    if request.method == "GET":
        print('get')
        return render(request, 'temp_login.html')

    elif request.method == "POST":
        print('post')
        user_id = request.POST.get('id')
        user_pw = request.POST.get('password')

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user=user)
            user = User.objects.get(username=user_id)
            context = {
                'user1': user
            }
            return render(request, 'temp_users.html', context)
        else:
            return redirect('login_url')

