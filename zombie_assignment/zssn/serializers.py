from rest_framework import serializers
from zssn.models import Survivor, Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ['id',]


class SurvivorSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Survivor
        fields = ['id', 'name', 'age', 'gender', 'location']

    def create(self, data):
        try:
            location_data = data.pop('location')
            location = Location.objects.create(**location_data)
            survivor = Survivor.objects.create(**data, location=location)
            return survivor

        except Exception as e:
            raise Exception(f'Error while creating new object for Survivor: {e}')

    def update(self, instance, data):
        try:
            location = data.pop('location')
            instance.email = data.get('name', instance.email)
            instance.content = data.get('age', instance.content)
            instance.created = data.get('gender', instance.created)

            instance.location.delete()
            instance.location = Location.objects.create(**location)

            instance.save()
            return instance
        
        except Exception as e:
            raise Exception(f'Error while updating data for Survivor Object: {e}')