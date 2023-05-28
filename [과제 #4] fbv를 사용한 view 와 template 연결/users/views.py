from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list1(request):
    name ='공유'
    return HttpResponse('''
    <h1> hello, </h1> 
    <p> {name} </p>
    <p> 반가워요 </p>'''.format(name=name))

def post_list2(request):
    name ='홍철'
    return render(request, 'index.html', {'name': name})

