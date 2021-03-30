import logging
import traceback
from django.shortcuts import render
import googlemaps
import requests
import json
from django.http.response import HttpResponse
from django.http import JsonResponse

GMAPS_API_KEY = "AIzaSyB4iPZ7A8FjvyWvoiPse3ZLYYP8cxkiE3E"
GMAPS_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
GMAPS_PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo"
GMAPS_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

gmaps = googlemaps.Client(key=GMAPS_API_KEY)

logger = logging.getLogger(__name__)


def OrangeHome(request):
    return render(request, "OrangeHome.html")


def HotelResults(request, place):
    try:
        if request.method == "GET":
            payload = {"key": GMAPS_API_KEY, "query": "hotels in " + place}
            gmap_request = requests.get(GMAPS_SEARCH_URL, params=payload)
            gmap_response = gmap_request.json()

            return JsonResponse(gmap_response, safe=False)

    except Exception as error:
        logger.error(traceback.format_exc())
        return HttpResponse(error)


def GetPhotos(request, placeId):
    try:
        if request.method == "GET":
            payload = {"key": GMAPS_API_KEY, "place_id": placeId,
                       "fields": "name,rating,photos"}
            gmap_request = requests.get(GMAPS_DETAILS_URL, params=payload)
            gmap_response = gmap_request.json()

            return JsonResponse(gmap_response, safe=False)

    except Exception as error:
        logger.error(traceback.format_exc())
        return HttpResponse(error)


def GetReviews(request, placeId):
    try:
        if request.method == "GET":
            payload = {"key": GMAPS_API_KEY, "place_id": placeId,
                       "fields": "name,rating,reviews"}
            gmap_request = requests.get(GMAPS_DETAILS_URL, params=payload)
            gmap_response = gmap_request.json()

            return JsonResponse(gmap_response, safe=False)

    except Exception as error:
        logger.error(traceback.format_exc())
        return HttpResponse(error)


def GetDetails(request, placeId):
    try:
        if request.method == "GET":
            payload = {"key": GMAPS_API_KEY, "place_id": placeId,
                       "fields": "name,rating,formatted_phone_number,photos,reviews"}
            gmap_request = requests.get(GMAPS_DETAILS_URL, params=payload)
            gmap_response = gmap_request.json()

            return JsonResponse(gmap_response, safe=False)

    except Exception as error:
        logger.error(traceback.format_exc())
        return HttpResponse(error)
