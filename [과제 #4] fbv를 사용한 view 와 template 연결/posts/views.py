from django.shortcuts import render

# Create your views here.


app_name ="liongram"

def home(request):
    return render (request, 'home.html')

def post1(request):
    return render (request, 'post1.html')

def post2(request):
    return render (request, 'post2.html')