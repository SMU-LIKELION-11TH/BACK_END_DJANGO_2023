from django.shortcuts import render
from django.http import HttpResponse

def post_view(request):
    return render(request, 'temp_posts', {''})
