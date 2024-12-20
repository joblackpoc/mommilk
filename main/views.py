from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Post, Infomation
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import conf
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('id')[:4]
    features = Post.objects.all().order_by('-id')[:3]
    infos = Infomation.objects.all().order_by('id')[:4]
    context = {'posts': posts,
               'features': features,
               'infos': infos}

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

# def post_list(request):
#   posts = Post.objects.all()
#   return render(request, 'post_list.html', {'posts': posts})

class PostListView(ListView):
    paginate_by = 6
    model = Post
    template_name = 'post_list.html'
    ordering = ['-id']
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

class InfoListView(ListView):
    paginate_by = 8
    model = Infomation
    template_name = 'info_list.html'
    ordering = ['-id']
def info_detail(request, pk):
    info = get_object_or_404(Infomation, pk=pk)
    return render(request, 'info_detail.html', {'info': info})



