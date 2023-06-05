from django.shortcuts import render, redirect
from reply.forms import ReplyForm
from post.models import Post

def create_reply(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # 답글 작성 처리 로직 작성
            # ...
            return redirect('post_detail', post_id=post.id)  # 답글 작성 후 이동할 URL
    else:
        form = ReplyForm()
    return render(request, 'create_reply.html', {'form': form, 'post': post})
