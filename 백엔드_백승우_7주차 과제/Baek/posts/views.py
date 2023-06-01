from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import Post
from users.models import User
from comments.models import Comment


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts_detail.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['post_id'])
        return context

class CategoryView(ListView):
    model = Post
    template_name = 'posts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list1'] = Post.objects.filter(category=1)
        context['post_list2'] = Post.objects.filter(category=2)
        context['post_list3'] = Post.objects.filter(category=3)
        context['post_list4'] = Post.objects.filter(category=4)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts_list.html'
    fields = ['category', 'title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.object.id
        return reverse('post_detail', kwargs={'post_id': post_id})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts_detail.html'
    template_suffix_name = 'posts_detail.html'
    fields = ['title', 'content']
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        post_id = self.object.id
        return reverse('post_detail', kwargs={'post_id': post_id})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('post_list')
    pk_url_kwarg = 'post_id'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CommentCreateView(LoginRequiredMixin, View):
    def get(self, post_id):
        return redirect('post_detail', post_id=post_id)

    def post(self, request, post_id):
        content = request.POST.get('comment_content')
        user = request.user
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(content=content, user=user, post=post)
        comment.save()
        return redirect('post_detail', post_id=post_id)

class CommentUpdateView(LoginRequiredMixin, View):
    def get(self, comment_id):
        comment = Comment.objects.get(id=comment_id)
        return redirect('post_detail', post_id=comment.post.id)

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        if request.user == comment.user:

            content = request.POST.get('comment_new_content')

            comment.content = content
            comment.save()

            return redirect('post_detail', post_id=comment.post.id)
        return redirect('post_detail', post_id=comment.post.id)
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'posts_detail.html'
    pk_url_kwarg = 'comment_id'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.object.post_id})