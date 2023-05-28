from django.shortcuts import render
from .models import Post

# Create your views here.


app_name ="lionlog"

def home(request):
    return render(request, 'home.html')

def post1(request):
    post1 = Post.objects.all()
    context = {
        'post1': post1,
    }
    return render (request, 'post1.html', context)







    # return render (request, 'post1.html', {'texts': post_text1})

def post2(request):
    # post_title2 = request.Post.get(id=2)
    # post_text2 = request.Post.get(id=2)
    #
    # post_title2 = request.Post['title']
    # post_text2 = request.Post['text']
    # return render (request, 'post2.html', {'title': post_title2})
    # return render (request, 'post1.html', {'text': post_text2})
