from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from comment.models import Comment
from reply.models import Reply
from django.contrib.auth.decorators import login_required
from post.forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post.html', context)

def post_detail(request,id):
    detail = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=detail)
    reply = Reply.objects.all()
    context = {
        'detail': detail,
        'comments': comments,
        'reply': reply
    }
    return render(request, '3월 일기.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def update_post(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', post_id=post.id)
        else:
            form = PostForm(instance=post)
        return render(request, 'update_post.html', {'form': form, 'post': post})
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')



