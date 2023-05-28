from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login




def user_login(request):
    if request.method == "GET":
        return render(request, 'log-in.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'LIKELION.html')
        else:
            return redirect('log-in.html')
def user_main():
    return redirect('LIKELION.html')





