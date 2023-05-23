from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'method': request.method,
        'user': request.user,
        'temp': 'welcome!',
    }
    return render(request, 'template/jinha.html', context)
