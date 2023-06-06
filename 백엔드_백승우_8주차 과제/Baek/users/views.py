from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# def user_detail(request):
#     if request.user.is_authenticated:
#
#         return render(request, 'users_detail.html')
#     else:
#         return redirect('login_view')
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users_detail.html'
    #context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

# def login_view(request):
#     if request.method == "GET":
#
#         return render(request, 'users_login.html')
#
#     elif request.method == "POST":
#
#         user_id = request.POST.get('username')
#         user_pw = request.POST.get('password')
#
#         user = authenticate(request, username=user_id, password=user_pw)
#
#         if user is not None:
#             login(request, user=user)
#             return redirect('user_detail')
#         else:
#             return redirect('login_view')
class UserLoginView(View):
    template_name = 'users_login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user=user)
            return redirect('user_detail')
        else:
            return redirect('login_view')
