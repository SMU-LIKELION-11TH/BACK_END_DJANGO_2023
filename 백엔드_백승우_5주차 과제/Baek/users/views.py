from django.shortcuts import render

def users_view(request):
    username = 'Baek'
    return render(request, 'temp_users.html', {'username': username})

