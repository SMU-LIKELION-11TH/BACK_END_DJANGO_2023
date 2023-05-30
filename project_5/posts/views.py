from django.shortcuts import render
from .models import Post, Comment, Reply
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from  django.urls import  reverse_lazy


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

#
# #cbv
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
    success_url = reverse_lazy('posts:post1')

class Post_update(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields= ["title", "writer", "image", "text", "created_at", "views"]
    success_url = reverse_lazy('posts:post1')

class Post_delete(DeleteView):
    model = Post
    template_name = 'post_update.html'
    fields= ["title", "writer", "image", "text", "created_at", "views"]
    success_url = reverse_lazy('posts:post1')

# //////////////////
class Comment_create(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields= ["text", "created_at"]
    success_url = reverse_lazy('posts:comment1')

class Comment_update(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields= ["text", "created_at"]
    success_url = reverse_lazy('posts:comment1')

<<<<<<< Updated upstream
class Comment_delete(DeleteView):
    model = Comment
    template_name = 'comment_update.html'
    fields= ["text", "created_at"]
    success_url = reverse_lazy('posts:comment1')

# //////////////////
class Reply_create(CreateView):
    model = Reply
    template_name = 'reply_create.html'
    fields= ["text", "created_at"]
    success_url = reverse_lazy('posts:reply1')

class Reply_delete(DeleteView):
    model = Reply
    template_name = 'reply_update.html'
    fields= ["text", "created_at"]
    success_url = reverse_lazy('posts:reply1')
=======
# class PostlistView(TemplateView):
#     template_name = "post_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["latest_posts"] = Post.objects.all()
#         return context

#

>>>>>>> Stashed changes


# class PostCreateView(CreateView):
#     model = Post
#     fields= ["title", "writer", "image", "text", "created_at", "views"]
#     template_name_suffix = "post_create.html"
#
#
#
# class CommentCreateView(CreateView):
#     model = Comment
#     fields= ["text", "created_at"]
#     template_name_suffix = "post_create.html"




# def post_create(request):
#     # form 요청, 데이터 생성
#     if request.method == 'GET':
#         return render (request, 'post_create.html')
#     else:
#         content = request.POST.get('content')
#         print(content)
#         Post.objects.create(
#             content= content,
#             # writer = request.user
#         )
#         return redirect('index')
#
#
# # class post_detail_view???
# # def post_detail(request, id):
# #     return render(request, 'post_create.html')
#
# def post_update(request, id):
#     post1 = Post.objects.get(id=id)
#     if request.method == 'GET':
#         context = {'post1':post1}
#         return render(request, 'post_create.html', context)
#     elif request.method =='POST':
#         pass
#
#
# def post_delete(request, id):
#     return render(request, 'post_create.html')
