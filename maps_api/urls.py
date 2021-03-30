from django.urls import path
from .views import HotelResults, GetDetails, GetPhotos, GetReviews
from .views_drf import HotelResults as drfHotelResults, CountryList, CountryDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("normal_api/<str:place>/", HotelResults),
    path("photos/<slug:placeId>/", GetPhotos),
    path("reviews/<slug:placeId>/", GetReviews),
    path("details/<slug:placeId>/", GetDetails),
]

# DJANGO REST FRAMWEWORK URLS
urlpatterns += [
    path("drf_api/countries/", CountryList.as_view()),
    path("drf_api/cities/<str:country>/", CountryDetail.as_view()),

    path("drf_api/hotels/<str:place>/", drfHotelResults.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
