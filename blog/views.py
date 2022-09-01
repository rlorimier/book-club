from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'details.html', {'post': post})


def about(request):
    aboutus = get_object_or_404(Post)
    return render(request, 'about.html', {'aboutus': aboutus})
