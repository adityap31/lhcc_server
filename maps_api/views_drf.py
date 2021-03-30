from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from maps_api.serializers import CountrySerializer, CountryCitySerializer
from maps_api.models import Country
from rest_framework.permissions import AllowAny

GMAPS_API_KEY = "AIzaSyD3geBfyCxvU-U5PnVK0PCEVXctJ9zxq5w"
GMAPS_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"


class HotelResults(APIView):
    def get(self, request, place="Mumbai", format=None):
        payload = {"key": GMAPS_API_KEY, "query": "hotels in " + place}
        gmap_request = requests.get(GMAPS_SEARCH_URL, params=payload)
        gmap_response = gmap_request.json()

        return Response(gmap_response)


class CountryList(APIView):
    """
    List all countries, or create a new country.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetail(APIView):
    """
    Retrieve, update or delete a country instance.
    """

    permission_classes = [AllowAny]

    def get_object(self, country):
        try:
            return Country.objects.get(name=country)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, country, format=None):
        country = self.get_object(country)
        serializer = CountryCitySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
