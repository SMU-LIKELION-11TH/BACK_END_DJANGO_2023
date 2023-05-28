from django.shortcuts import render, redirect
from .models import Post
from users.models import User
from comments.models import Comment
from recomments.models import Recomment

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.filter(post_id=post_id)
    #recomment = Recomment.objects.filter(comment_id=comment1.id)

    context = {
        'post': post,
        'comment': comment,
        #, 'recomment': recomment
    }

    return render(request, 'detail.html', context)

def category_view(request, user_id):

    user = User.objects.get(id=user_id)
    post_list1 = Post.objects.filter(category=1)
    post_list2 = Post.objects.filter(category=2)
    post_list3 = Post.objects.filter(category=3)
    post_list4 = Post.objects.filter(category=4)

    context = {
        'user': user,
        'post_list1': post_list1,
        'post_list2': post_list2,
        'post_list3': post_list3,
        'post_list4': post_list4,
    }

    return render(request, 'list.html', context)

def post_create(request, user_id):
    user = User.objects.get(id=user_id)
    title = request.POST.get('title')
    category = request.POST.get('category')
    content = request.POST.get('content')

    post = Post.objects.create(category=category, title=title, content=content, user=user)
    post.save()

    return redirect('post_detail', post_id=post.id)

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
            return redirect('category_detail', user_id=request.user.id)

    return redirect('post_detail', post_id=post.id)

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')

            post.title = title
            post.content = content
            post.save()

            return redirect('post_detail', post_id=post.id)

    return redirect('post_detail', post_id=post.id)

def comment_create(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    content = request.POST.get('comment_content')

    comment = Comment.objects.create(content=content, user=user, post=post)
    comment.save()

    return redirect('post_detail', post_id=post.id)

def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('post_detail', post_id=comment.post.id)

    return redirect('post_detail', post_id=comment.post.id)

def comment_update(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.user == comment.user:
        if request.method == 'POST':
            content = request.POST.get('comment_new_content')

            comment.content = content
            comment.save()

            return redirect('post_detail', post_id=comment.post.id)

    return redirect('post_detail', post_id=comment.post.id)


