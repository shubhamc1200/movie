from django.shortcuts import render,redirect
from .models import Movie
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm
from django.template.defaultfilters import slugify


# Create your views here.
def movie_list(request):
    movies=Movie.objects.all().order_by('date')

    return render(request,'movies/movies_list.html',{'movies':movies})

def movie_details(request,slug):
    movie=Movie.objects.get(slug=slug)
    return render(request,'movies/movie_details.html',{'movie':movie})

def movie_create(request):

    if request.method=='POST':
        form=forms.CreateMoviePage(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            instance.slug #for slugifying title
            return redirect('movies:list')
    else:
        form=forms.CreateMoviePage()
    return render(request,'movies/movie_create.html',{'form':form})

def add_comment_to_movie(request,slug):
    movie = Movie.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author=str(request.session["name_user"])
            comment.save()
            return redirect('movies:details', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'movies/add_comment_to_movie.html',{'form': form})

def movie_delete(request,slug):
    movie = Movie.objects.get(slug=slug)

    movie.delete()
    return redirect('movies:list')
    return render(request,'movies/movie_update.html',{'form':form,'movie':movie})

def movie_update(request,slug):
    movie = Movie.objects.get(slug=slug)
    if request.method=='POST':
        form=forms.CreateMoviePage(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            f=form.save(commit=False)
            f.author=request.user
            f.save()
            return redirect('movies:details', slug=slug)
    else:
        form=forms.CreateMoviePage()
    return render(request,'movies/movie_update.html',{'form':form,'movie':movie})
