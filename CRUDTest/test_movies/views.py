from django.shortcuts import render, redirect

import proyectoa_web.utils
from .forms import MovieForm

from .models import Movie,Reaction
from django.contrib import messages

# Create your views here.


def add(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    else:
      if request.POST:
          messages.error(request, 'Error in movie data')
      else:
          messages.info(request, 'Insert Movie data')
          form = MovieForm()

    context = {'form': form }
    return render(request, 'movie.html', context)

def show(request):
    movies = Movie.objects.all()
    return render(request, "main_view.html", {'movies': movies})

def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("/")

def edit(request, id):
    movie = Movie.objects.get(id=id)
    return render(request,'movie_edit.html', {'movie':movie})

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST, instance = movie)
    if form.is_valid():
        form.save()
        return redirect("/")
    else:
        messages.error(request, 'Error in Movie data')
        form = MovieForm()

    context = {'form': form}
    return render(request, 'movie_edit.html', context)
def add_reaction(request,reaction_type,movieId):
    reaction = Reaction(type=reaction_type,movieId=movieId)
    reaction.save()

    return redirect("/")


