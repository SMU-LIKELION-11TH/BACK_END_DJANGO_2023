from django.shortcuts import render


# Create your views here.

def user_list(request):
    return render(request, 'log-in.html')

def user_list2(request):
    return render(request, 'LIKELION.html')