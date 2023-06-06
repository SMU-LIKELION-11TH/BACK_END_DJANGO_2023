from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment, Reply
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django import forms
from django.views.generic import UpdateView
from datetime import datetime
from django.urls import reverse_lazy


# Create your views here.


app_name ="post"

#templateView
def home(request):
    return render(request, 'home.html')

# fbv
# def post1(request, id):
#     post1 = Post.objects.get(pk=id)
#     comment1 = Comment.objects.filter(post = post1)
#     reply1 = Reply.objects.all()
#
#     context = {
#         'post1': post1,
#         'comment1': comment1,
#         'reply1': reply1,
#     }
#     return render (request, 'post1.html', context)

#cbv
class PostView(DetailView):
    model = Post
    template_name = 'post1.html'
    context_object_name = 'post1'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post1 = self.object
        comment1 = Comment.objects.filter(post=post1)
        reply1 = Reply.objects.all()
        context['comment1'] = comment1
        context['reply1'] = reply1
        return context


class Post_create(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields= ["title", "writer", "image", "text", "created_at", "views"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class':'form-control', 'rows':10})
        }
        labels = {
            'title': '제목',
            'text': '내용'
        }


class Post_update(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields= ["text"]
    pk_url_kwarg = 'id'
    def get_success_url(self):
        return reverse_lazy("post:DetailView",args=[self.get_object().pk])
    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        return super.form_valid(form)

# class Post_delete(DeleteView):
#     model = Post
#     template_name = 'post1.html'
#     def get(self, request, *args, **kwargs ):
#         return self.post(request, *args, *kwargs)
#     def get_success_url(self):
#         return reverse_lazy('home')



# delete
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'post_delete.html', {'post': post})



# //////////////////




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class Comment_create(CreateView):
    model = Comment
    from_class = CommentForm
    template_name = 'comment_create.html'
    fields= ["text","created_at"]
    # success_url = reverse_lazy('posts:comment1')

class Comment_update(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields= ["text", "created_at"]
    def get_success_url(self):
        return reverse_lazy('comment-list', kwargs={'id': self.object.id})

class Comment_deltete(DeleteView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ["text", "created_at"]
    success_url = reverse_lazy('form')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post.id']
        return super().form_valid(form)
# //////////////////

class Reply_create(CreateView):
    model = Reply
    template_name = 'reply_create.html'
    fields= ["text", "created_at"]
    # success_url = reverse_lazy('posts:reply1')

class Reply_delete(DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    fields= ["text", "created_at"]
    # success_url = reverse_lazy('posts:reply1')




