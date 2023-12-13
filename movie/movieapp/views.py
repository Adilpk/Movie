from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie_list
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = movie_list.objects.all()
    context = {
        'movies': movie
    }
    return render(request, 'index.html', context)


def details(request, m_id):
    mv = movie_list.objects.get(id=m_id)
    return render(request, 'details.html', {'mt': mv})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('mname')
        decs = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        mv = movie_list(name=name, desc=decs, year=year, img=img)
        mv.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = movie_list.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'fr': form, 'mvv': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = movie_list.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
