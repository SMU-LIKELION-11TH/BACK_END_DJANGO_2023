from django.shortcuts import render
from .models import Users, Stores, Menus

def homepage(request):
    users = Users.objects.values('username', 'address').first()
    stores = Stores.objects.values('store_link', 'store_name').first()

    context = {
        "username": users['username'] if users else None,
        "address": users['address'] if users else None,
        "store_link": stores['store_link'] if stores else None,
        "store_name": stores['store_name'] if stores else None,
    }

    return render(request, 'home.html', context)
def store(request):
    stores = Stores.objects.values('store_name', 'store_address').first()
    menus = Menus.objects.values('menu_name', 'menu_price')

    context = {
        "store_name": stores['store_name'] if stores else None,
        "address": stores['store_address'] if stores else None,
        "menu": menus['menu_name'] if menus else None,
        "price": menus['menu_price'] if menus else None,
    }

    return render(request, 'store.html', context)

def login(request):
    if request.method == "POST":
        return redirect('homepage')
    else:
        return render(request, 'login.html')