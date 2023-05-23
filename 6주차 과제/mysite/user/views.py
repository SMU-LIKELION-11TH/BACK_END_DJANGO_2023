from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.

def user_login(request):
    if request.method == "GET":
        return render(request, 'log-in.html')
    elif request.method == "POST":
        username = request.POST.get('username')
       password= request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user=user)
        return redirect('Likelion.html')

    else:
        messages.error(request, 'ID 혹은 비밀번호 오류입니다.')
        return redirect('log-in.html')
)


def user_main(request):
    return render(request, 'LIKELION.html',name='home')