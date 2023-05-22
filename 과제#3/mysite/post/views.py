from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_list(request):
    name ='공유'
    return HttpResponse(''' <h1> hello </h1> <p>{name}</p> <p>반가워요</p>'''.format(name=name))

def homepage(request):
    name = '배달의민족'
    return render(request, 'home.html', {'name':name})
5
def store_1(request):
    name = '부대통령'
    return render(request, 'store1.html', {'name':name})

def store_2(request):
    name = '치즈밥있슈'
    return render(request, 'store2.html', {'name':name})