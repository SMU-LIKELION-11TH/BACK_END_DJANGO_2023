from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
def users_view(request):
    user1 = User.objects.get(id=1)

    context = {
        'user1': user1
    }

    return render(request, 'temp_users.html', context)

def login_view(request):
    if request.method == "GET":
        return render(request, 'temp_login.html')

    elif request.method == "POST":
        user_id = request.POST.get('id')
        user_pw = request.POST.get('password')

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user=user)
            return render(request, 'temp_users.html')
        else:
            return redirect('login_url')
