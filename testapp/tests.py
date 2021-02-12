from django.test import TestCase
from .models import (
    User, 
    Group,
    Location,
    CountryCode,
    Connector,
    Tariff,
    ChargePoint,
)
from .factories import (
    UserFactory, 
    GroupFactory,
    LocationFactory,
    CountryCodeFactory,
    ConnectorFactory,
    TariffFactory,
    ChargePointFactory
)

class FactoriesTestCase(TestCase):
    def setUp(self):
        group = GroupFactory()
    
    def test_create_user(self):
        user = UserFactory()
        user_count = User.objects.count()
        group_count = Group.objects.count()
        self.assertIs(user_count, 1)
        self.assertIs(user.groups.count(), 0)
        self.assertIs(group_count, 1)

        group = GroupFactory()
        user = UserFactory()
        user.groups.add(group)
        user_count = User.objects.count()
        group_count = Group.objects.count()
        self.assertIs(user_count, 2)
        self.assertIs(user.groups.count(), 1)
        self.assertIs(group_count, 2)
    
    def test_create_location(self):
        location = LocationFactory()
        location_count = Location.objects.count()
        self.assertIs(location_count, 1)

    def test_create_country_code(self):
        country_code = CountryCodeFactory()
        country_code_count = CountryCode.objects.count()
        self.assertIs(country_code_count, 1)
    
    def test_create_connector(self):
        connector = ConnectorFactory()
        connector_count = Connector.objects.count()
        self.assertIs(connector_count, 1)
        self.assertIs(connector.tariffs.count(), 0)

        tariff = TariffFactory()
        connector = ConnectorFactory()
        connector.tariffs.add(tariff)
        connector_count = Connector.objects.count()
        self.assertIs(connector_count, 2)
        self.assertIs(connector.tariffs.count(), 1)
    
    def test_create_tariff(self):
        tariff = TariffFactory()
        tariff_count = Tariff.objects.count()
        self.assertIs(tariff_count, 1)
        self.assertIs(tariff.connectors.count(), 0)

        connector = ConnectorFactory()
        tariff = TariffFactory()
        tariff.connectors.add(connector)
        tariff_count = Tariff.objects.count()
        self.assertIs(tariff_count, 2)
        self.assertIs(tariff.connectors.count(), 1)
    
    def test_create_charge_point(self):
        charge_point = ChargePointFactory()
        charge_point_count = ChargePoint.objects.count()
        location_count = Location.objects.count()
        self.assertIs(charge_point_count, 1)
        self.assertIs(charge_point.groups.count(), 0)
        self.assertIs(location_count, 1)

        location = Location.objects.first()
        self.assertIs(location.charge_points.count(), 1)
        self.assertIs(len(location.groups), 0)

        group = GroupFactory()
        charge_point.groups.add(group)
        group_count = Group.objects.count()
        self.assertIs(group_count, 2)
        self.assertIs(len(location.groups), 1)
        self.assertIs(charge_point.groups.count(), 1)



class GroupTestCase(TestCase):
    pass