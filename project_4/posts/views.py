from django.shortcuts import render
from .models import Post, Comment, Reply

# Create your views here.


app_name ="lionlog"

def home(request):
    return render(request, 'home.html')

def post1(request, id):
    post1 = Post.objects.get(pk=id)
    comment1 = Comment.objects.filter(post = post1)
    reply1 = Reply.objects.all()

    context = {
        'post1': post1,
        'comment1': comment1,
        'reply1': reply1,
    }
    return render (request, 'post1.html', context)


