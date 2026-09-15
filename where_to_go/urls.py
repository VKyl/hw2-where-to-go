
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.places, name='places'),
    path('places/new/', views.new_place, name='new_place'),
    path('places/<str:place_id>/', views.place_detail, name='place_detail'),
]