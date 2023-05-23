from django.shortcuts import render
from .models import Post
from users.models import User
from comments.models import Comment
from recomments.models import Recomment

def post_view(request):
    post1 = Post.objects.get(id=1)
    comment1 = Comment.objects.get(id=1)
    recomment1 = Recomment.objects.get(id=1)

    context = {
        'post1': post1,
        'comment1': comment1,
        'recomment1': recomment1
    }

    return render(request, 'temp_posts.html', context)

def category_view(request):
    post_list1 = Post.objects.filter(category=1)
    post_list2 = Post.objects.filter(category=2)
    print(post_list1)
    context = {
        'post_list1': post_list1,
        'post_list2': post_list2,
    }

    return render(request, 'temp_category.html', context)