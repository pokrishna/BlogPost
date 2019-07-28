from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# def home(request):
#     context={'posts':Post.objects.all()}
#     return render(request,'Blog/home.html',context)
#
# def about(request):
#     return render(request,'Blog/about.html',{'title':'About Blog'})
# def home(request):
#     context={'posts':Post.objects.all()}
#     return render(request,'Blog/home.html',context)
#
# def about(request):
#     return render(request,'Blog/about.html',{'title':'About Blog'})


def home(request):
    context={'posts':Post.objects.all()}
    return render(request,'Blog/home.html',context)

def about(request):
    return render(request,'Blog/about.html',{'title':'About Blog'})
