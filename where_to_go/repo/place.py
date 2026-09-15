from ..models.place import Place

class PlacesRepository:
    __COLLECTION_NAME = 'places'
    __DEFAULT_PLACES = [
         
    ]

    def _get_collection(self, session) -> list[dict]:
        return session.setdefault(self.__COLLECTION_NAME, [

        ])

    def get_all_places(self, session) -> list[Place]:
        return [Place.deserialize(place) for place in self._get_collection(session)]

    def get_place(self, session, place_id: str) -> Place | None:
        for place in self._get_collection(session):
            if place['id'] == place_id:
                return Place.deserialize(place)
        return None

    def add_place(self, session, place: Place):
        places = self._get_collection(session)
        session[self.__COLLECTION_NAME] = places + [place.serialize()]