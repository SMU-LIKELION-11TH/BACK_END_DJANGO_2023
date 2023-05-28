from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    name = 'username'
    return HttpResponse(''' <h1> 로그인에 성공하셨습니다. </h1> 
                            <p>환영합니다. {name} 님</p> 
                            <p>반가워요</p>'''.format(name=name))
def homepage(request):

    if request.method == "GET":
        context = {
        "username":request.user,
        "address" :'서울특별시 종로구 홍지문2길 20',
        }
        return render(request, 'home.html', context)

    if request.method == "POST":
        return HttpResponse("")

def store_1(request):
    name = '부대통령'
    return render(request, 'store1.html', {'name':name})

def store_2(request):
    name = '치즈밥있슈'
    return render(request, 'store2.html', {'name':name})

def login(request):
    name = '로그인'
    return render(request, 'login.html', {'name':name})