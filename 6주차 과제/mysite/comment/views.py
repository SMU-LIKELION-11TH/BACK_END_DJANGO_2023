# views.py

from django.shortcuts import render, redirect
from .models import  Comment


def post_detail(request):
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_comment.html', {'post': post, 'comments': comments})

def add_comment(request, post_id):
    if request.method == 'POST':
        detail = request.POST['detail']
        comment = Comment(post=post, detail=detail)
        comment.save()
    return redirect('post_detail', post_id=post_id)

def comment_created_at(request):
    comments = Comment.objects.all()
    created_at_list = [comment.created_at for comment in comments]
    context = {
        'created_at_list': created_at_list
    }
    return render(request, 'comments.html', context)

