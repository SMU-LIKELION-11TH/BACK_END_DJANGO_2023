from django.shortcuts import render
from .models import Post, Comment, Reply

# Create your views here.


app_name ="lionlog"

def home(request):
    return render(request, 'home.html')

def post1(request):
    post1 = Post.objects.get(pk=1)
    comment1 = Comment.objects.get(post = post1)
    reply1= Reply.objects.get(comment = comment1)

    context = {
        'post1': post1,
        'comment1': comment1,
        'reply1': reply1,
    }
    return render (request, 'post1.html', context)



def post2(request):
    post2 = Post.objects.get(pk=2)
    comment2 = Comment.objects.get(post=post2)
    reply2= Reply.objects.get(comment = comment2)

    context2 = {
        'post2' : post2,
        'comment2': comment2,
        'reply2': reply2,
    }

    return render (request, 'post2.html', context2)

