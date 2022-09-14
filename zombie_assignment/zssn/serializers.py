from typing import Dict
from rest_framework import serializers
from zssn.models import Survivor, Location

class LocationSerializer(serializers.ModelSerializer):
    """
    A class to serialize Location model
    """

    class Meta:

        # model to serialize
        model = Location

        # exclude fields from result
        exclude = ['id',]


class SurvivorSerializer(serializers.ModelSerializer):
    """
    A class to serialize Survivor model
    """

    # Location serializer for location field in Survivor model
    location = LocationSerializer()

    class Meta:
        # model to serialize
        model = Survivor

        # fields to include in result
        fields = ['id', 'name', 'age', 'gender', 'location']

    def create(self, data: Dict) -> Survivor:
        """
        Method to create new 
        """
        try:

            # extract location from data
            location_data = data.pop('location')

            # Create location 
            location = Location.objects.create(**location_data)

            # Create Survivor
            survivor = Survivor.objects.create(**data, location=location)

            # return survivor
            return survivor

        except Exception as e:
            raise Exception(f'Error while creating new object for Survivor: {e}')

   