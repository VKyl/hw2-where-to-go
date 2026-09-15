from ..models.place import Place

class PlacesRepository:
    __COLLECTION_NAME = 'places'
    __DEFAULT_PLACES = [
        {
            'id': '683d8100a272496d891b548b83a9275d',
            'name': 'КМЦ',
            'rating': 5,
            'description': 'Місце могилянської сили (і фішників на деревах)',
            'place_type': 'тусічне',
            'location': 'КМЦ',
            'photo': 'gopher-train.png',
        },
        {
            'id': 'f555106bf9e34c19a9f7ce06bcdbd2c1',
            'name': 'Коморка Fido',
            'rating': 4,
            'description': 'Чудове місце щоб повтикать на парах, з мінусів можуть змусити писати smarkukma',
            'place_type': 'ретріт',
            'location': 'КМА плац 2',
            'photo': 'gopher-train.png',
        },
        {
            'id': 'c66ad225209d47068342e0afa40c74be',
            'name': 'Староакадемічний корпус',
            'rating': 5,
            'description': 'Там гіркий зробили, смачна кава',
            'place_type': 'історичне',
            'location': 'вул. Сковороди, 2',
            'photo': 'gopher-train.png',
        },
        {
            'id': '1b7b9be6e98540c8acd391c49d0f73a8',
            'name': 'Контрактова площа',
            'rating': 4,
            'description': 'Найкраще місце подихати повітрям між парами (але частіше подіками і цигарками)',
            'place_type': 'площа',
            'location': 'Поділ',
            'photo': 'gopher-train.png',
        },
        {
            'id': '10fa68a3f8304b1fb5cd95d8be389c8e',
            'name': 'Дніпровська набережна',
            'rating': 5,
            'description': 'Класно прогулятися, можна сходити в мак',
            'place_type': 'набережна',
            'location': 'Поділ, набережна',
            'photo': 'gopher-train.png',
        },
        {
            'id': 'e6ee10a076a74394a0c83d33e416ac8c',
            'name': 'Наукова бібліотека НаУКМА',
            'rating': 4,
            'description': 'Тут можна знайти книгу, тишу і надію на успішну сесію (але не на колках з теорії ймовірності)',
            'place_type': 'бібліотека',
            'location': 'вул. Волоська, 8-14',
            'photo': 'gopher-train.png',
        },
        {
            'id': '569d8b980514403d97452571b1275c27',
            'name': 'Аскольдова могила',
            'rating': 5,
            'description': 'Тихий парк над Дніпром',
            'place_type': 'парк',
            'location': 'Парк Слави',
            'photo': 'gopher-train.png',
        },
    ]

    def _get_collection(self, session) -> list[dict]:
        return session.setdefault(self.__COLLECTION_NAME, self.__DEFAULT_PLACES.copy())

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