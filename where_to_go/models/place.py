from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Place(models.Model):
    class PlaceType(models.TextChoices):
        RESTAURANT = 'restaurant', 'Restaurant'
        CAFE = 'cafe', 'Cafe'
        BAR = 'bar', 'Bar'
        PARK = 'park', 'Park'
        MUSEUM = 'museum', 'Museum'
        ATTRACTION = 'attraction', 'Attraction'
        OTHER = 'other', 'Other'

    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(blank=True)
    place_type = models.CharField(
        max_length=20, choices=PlaceType.choices, blank=True
    )
    location = models.CharField(max_length=255, blank=True)
    photo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def deserialize(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            rating=data.get('rating'),
            description=data.get('description'),
            place_type=data.get('place_type'),
            location=data.get('location'),
            photo=data.get('photo'),
        )

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'description': self.description,
            'place_type': self.place_type,
            'location': self.location,
            'photo': self.photo,
        }

    def __str__(self):
        return self.name
