from django.contrib import admin
from django.urls import path, include
from maps_api.views import OrangeHome

urlpatterns = [
    path('', OrangeHome),
    path('admin/', admin.site.urls),
    path('server/', include('maps_api.urls')),

]


admin.site.site_header = "OrangeHome Admin"
admin.site.site_title = "OrangeHome Admin Portal"
admin.site.index_title = "Welcome to OrangeHome Admin Portal"
