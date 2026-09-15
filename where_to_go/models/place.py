from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.dateparse import parse_datetime


class Place(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(blank=True)
    place_type = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=255, blank=True)
    photo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField()

    @classmethod
    def deserialize(cls, data: dict):
        created_at = data.get('created_at')
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            rating=data.get('rating'),
            description=data.get('description'),
            place_type=data.get('place_type'),
            location=data.get('location'),
            photo=data.get('photo'),
            created_at=parse_datetime(created_at) if created_at else None,
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
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return self.name
