from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "post/home.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_at = timezone.now()
            post.save()
            return redirect("post:home")
    else:
        form = PostForm()
    return render(request, "post/add_post.html", {"form": form})




