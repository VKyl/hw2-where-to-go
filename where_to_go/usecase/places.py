
import uuid

from ..models.place import Place
from ..forms.place import PlaceForm

class PlacesUseCase:
    def __init__(self, places_repository):
        self.places_repository = places_repository

    def add_place(self, session, form: PlaceForm) -> bool:
        if not form.is_valid():
            return False
        place = Place.deserialize({**form.cleaned_data, 'id': uuid.uuid4().hex})
        self.places_repository.add_place(session, place)
        return True

    def get_place(self, session, place_id: str) -> Place | None:
        return self.places_repository.get_place(session, place_id)

    def get_all_places(self, session) -> list[Place]:
        return self.places_repository.get_all_places(session)
       