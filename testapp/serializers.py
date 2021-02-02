from .models import User, Group, Location, CountryCode, ChargePoint
from rest_framework import serializers

from .enum_types import CountryList
from drf_writable_nested.serializers import WritableNestedModelSerializer


class GroupSerializer(serializers.ModelSerializer):
    
    #To remove unique validation.
    name = serializers.CharField(max_length=255)
    
    class Meta:
        model = Group
        fields = ["name"]

    """ def to_internal_value(self, data):
        data = {"name": data}
        return data """

    """ def to_representation(self, instance):
        if isinstance(instance, Group):
            return instance.name
        else:
            return super().to_representation(instance) """

    def save(self, **kwargs):
        location = kwargs.get('location')
        group_name = self.validated_data.get('name')
        group, created = Group.objects.get_or_create(name=group_name)
        if location is not None:
            charge_point = location.charge_points.first()
            if charge_point is None:
                charge_point = ChargePoint.objects.create(location=location)
            group.charge_points.add(charge_point)
        return group 

class UserSerializer(WritableNestedModelSerializer):
    groups_ = GroupSerializer(many=True, source="groups")

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups_']
    
    def to_internal_value(self, data):
        data['groups_'] = [{'name': group_name} for group_name in data.get('groups_')]
        data = super().to_internal_value(data)
        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['groups_'] = [group['name'] for group in ret['groups_']]
        return ret
    
    """ def save(self, **kwargs):
        groups = self.validated_data.get('groups')
        for group in groups:
            Group.objects.get_or_create(name=group) """

class CountryCodeSerializer(serializers.ModelSerializer):

    code = serializers.CharField(max_length=2)

    class Meta:
        model = CountryCode
        fields = ['code']
    
    def save(self, **kwargs):
        code = self.validated_data.get('code')
        country_code, created = CountryCode.objects.get_or_create(code=code)
        return country_code 

class LocationSerializer(WritableNestedModelSerializer):
    country_code = CountryCodeSerializer(many=False, required=True)
    groups = GroupSerializer(many=True, required=False)

    class Meta:
        model = Location
        fields = ["country_code", "groups"]
    
    def to_internal_value(self, data):
        country_code = data.get('country_code')
        if country_code:
            data['country_code'] = {'code': country_code}
        data['groups'] = [{'name': group_name} for group_name in data.get('groups')]
        data = super().to_internal_value(data)
        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        #country_code = ret.get('country_code')
        #if country_code is not None:
        #    ret['country_code'] = country_code.get('code')
        #ret['groups'] = [group['name'] for group in ret['groups']]
        return ret
    
    def save(self, **kwargs):
        groups = self.validated_data.pop('groups')
        location = super().save(**kwargs)
        if groups is not None:
            for group_data in groups:
                group_serializer = GroupSerializer(data=group_data)
                group_serializer.is_valid(raise_exception=True)
                group_serializer.save(location=location)

        return location
    
        
        


