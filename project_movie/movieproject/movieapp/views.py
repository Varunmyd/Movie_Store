from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import Movieform
from .models import Movie


# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        dis = request.POST.get('dis')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, dis=dis, year=year, img=img)
        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie1 = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html',{'movie':movie1})
