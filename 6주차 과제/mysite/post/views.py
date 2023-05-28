from django.shortcuts import render
from .models import Post
from comment.models import Comment
from reply.models import Reply

def post_title(request):
    titles = Post.objects.values_list('title', flat=True)
    context = {
        'titles': titles,
    }
    return render(request, 'post.html', context)

def post_detail(request,id):
    detail = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=detail)
    reply = Reply.objects.filter(post=detail)
    context = {
        'detail': detail,
        'comments': comments,
        'reply': reply
    }
    return render(request, '3월 일기.html', context)