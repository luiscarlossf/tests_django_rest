import factory
from faker import Faker

from testapp.models import (
    User, 
    Group,
    CountryCode,
    Location,
    Tariff,
    Connector,
    ChargePoint,

)

fake = Faker()

class CountryCodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CountryCode
    
    code = factory.LazyAttribute(lambda obj: fake.country_code())

class TariffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tariff

    name = factory.Sequence(lambda n : f"tariff_{n}")

class ConnectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Connector

    name = factory.Sequence(lambda n : f"connector_{n}")

    @factory.post_generation
    def tariffs(self, created, extracted, **kwargs):
        if not created:
            # Simple build, do nothing.
            return

        if extracted:
            for tariff in extracted:
                self.tariffs.add(tariff)

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    country_code = factory.SubFactory(CountryCodeFactory)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n : f"group_{n}")

class ChargePointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChargePoint
    
    location = factory.SubFactory(LocationFactory)
    
    @factory.post_generation
    def groups(self, created, extracted, **kwargs):
        if not created:
            # Simple build, do nothing.
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n : f"group_{n}")
    username = factory.Sequence(lambda n: f"{fake.user_name()}_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@miio.pt")

    @factory.post_generation
    def groups(self, created, extracted, **kwargs):
        if not created:
            # Simple build, do nothing.
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
