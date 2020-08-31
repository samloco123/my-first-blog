from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Skill, Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import *
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv_edit(request):
    if request.method == 'POST':
        if request.POST['skill_text'] != '':
            Skill.objects.create(text=request.POST['skill_text'])
            return redirect('/cv/edit/')
    
    skills = Skill.objects.all()
    works = Work.objects.all()
    educs = Education.objects.all()
    return render(request, 'blog/cv_edit.html', {'skills' : skills, 'works' : works, 'educs' : educs})

def cv_add_work(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_edit')
    else:
        form = WorkForm()
    return render(request, 'blog/cv_add_work.html', {'form': form})

def cv_add_educ(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_edit')
    else:
        form = EducationForm()
    return render(request, 'blog/cv_add_educ.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    else:
        posts = Post.objects.filter(status="Published")
    return render(request, 'blog/search_results.html', {'posts': posts})