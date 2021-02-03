from .models import User, Group, Location, CountryCode, Connector
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    UserSerializer, 
    GroupSerializer, 
    LocationSerializer, 
    CountryCodeSerializer, 
    ConnectorSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryCodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows country_codes to be viewed or edited.
    """
    queryset = CountryCode.objects.all()
    serializer_class = CountryCodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConnectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows connectors to be viewed or edited.
    """
    queryset = Connector.objects.all()
    serializer_class = ConnectorSerializer
    permission_classes = [permissions.IsAuthenticated]