from datetime import datetime

from django.test import TestCase, Client

# Create your tests here.
from core.models import User
from geo.models import Station, City, Region
from boxes.models import ContainerType, FreeContainer
from .models import BaseContainerRequest, FreeContainerRequest


def create_user():
    test = User(username="test", email="test@q.ru")
    test.save()
    return test


def fill_dicts():
    ContainerType(title="Обычный").save()
    ContainerType(title="Увеличенный").save()
    Region(title="Москва").save()
    Region(title="Московская область").save()
    Region(title="Ленинградская область").save()
    City(title="Москва", region_id=1).save()
    Station(title="Ярославский вокзал", city_id=1)
    Station(title="Ленинградский вокзал", city_id=1)
    City(title="Коломна", region_id=1).save()
    Station(title="Коломна", city_id=2).save()


class TestFreeContainerSearch(TestCase):
    def test_filter_dict(self):
        fill_dicts()
        user = create_user()
        client = Client()
        client.force_login(user)
        search = FreeContainerRequest(
            user=user,
            created=datetime.now(),
            count=5,
            date_from=datetime(year=2019, month=5, day=10),
            date_till=datetime(year=2019, month=6, day=15),
            type=ContainerType.objects.get(id=1)
        )
        search.save()
        search.location.add(Station.objects.get(id=1))
        self.assertDictEqual(search.filter_dict(), {
            'date_from': "2019-05-10",
            'date_till': "2019-06-15",
            'type': 1,
            'location': [1],
            'location__city': [],
            'location__city__region': [],
            'count': 5,
            'address': None
        })

