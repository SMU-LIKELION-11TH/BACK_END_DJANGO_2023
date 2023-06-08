from django.shortcuts import render
from .models import Stores, Menus
from .forms import OrderForm

def homepage(request):
    stores = Stores.objects.all()
    form = OrderForm()
    context = {
        "stores": stores,
        "form": form,
    }

    return render(request, 'home.html', context)
def store(request, id):
    store = Stores.objects.get(id=id)
    menus = Menus.objects.filter(store_name=id)
# get, filter ()안에 조건 씀, get은 조건에 맞는 한개, filter은 조건에 맞는 모든 것, 검색이 존재하냐 아니냐에 딸 사용용도가 다름 get은 id 사용
    context = {
        "store": store,
        "menus": menus,
    }

    return render(request, 'store.html', context)

def login(request):
    if request.method == "POST":
        return redirect('homepage')
    else:
        return render(request, 'login.html')