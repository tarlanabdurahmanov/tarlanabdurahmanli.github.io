from django.shortcuts import render, redirect
from core.models import *
# Create your views here.
from core.forms import *
from django.contrib.auth.decorators import login_required
from core.filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    posts = Post.objects.filter(active=True)
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    # page = request.GET.get('page',1)
    # paginator = Paginator(posts, 4)

    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'myFilter': myFilter,
    }
    return render(request, 'index.html', context)

@login_required(login_url="/home")
def post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)


def resume(request):
    return render(request, 'resume.html')
