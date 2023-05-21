from django.shortcuts import render


# Create your views here.

def post_list1(request):
    return render(request, 'post.html')
def post_list2(request):
    return render(request, '3월 일기.html')
def post_list3(request):
    return render(request, '4월 일기.html')
