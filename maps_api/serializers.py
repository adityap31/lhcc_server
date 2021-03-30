from .models import Country, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ["name"]


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ["name"]


class CountryCitySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Country
        fields = ["name", "cities"]
