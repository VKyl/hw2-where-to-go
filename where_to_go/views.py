from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms.place import PlaceForm
from .usecase.places import PlacesUseCase
from .repo.place import PlacesRepository
import random

def index(request):
    return render(request, 'index.html', {'page_title': 'About '})

def places(request):
    uc = PlacesUseCase(PlacesRepository())
    places = uc.get_all_places(request.session)
    return render(request, 'places.html', {'page_title': 'Places', 'places': places})

def new_place(request):
    uc = PlacesUseCase(PlacesRepository())
    if request.method != 'POST':
        return render(request, 'new_place.html', {'page_title': 'New Place', 'form': PlaceForm()})
    form = PlaceForm(request.POST)
    if uc.add_place(request.session, form):
        return redirect('places')
    return render(request, 'new_place.html', {'page_title': 'New Place', 'form': form})

def place_detail(request, place_id):
    uc = PlacesUseCase(PlacesRepository())
    place = uc.get_place(request.session, place_id)
    if place is None:
        return render(request, 'place.html', {'page_title': 'Place Not Found', 'place': None})
    return render(request, 'place.html', {'page_title': f'Place {place.name}', 'place': place})

def random_place(request):
    uc = PlacesUseCase(PlacesRepository())
    places = uc.get_all_places(request.session)
    if not places:
        return JsonResponse({'place': None})
    place = random.choices(places, weights=[place.rating for place in places], k=1)[0]
    return JsonResponse({'place': place.serialize()})
