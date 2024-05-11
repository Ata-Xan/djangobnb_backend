from django.urls import path
from . import api

urlpatterns = [
    # the api.site.urls is the admin panel


    path('', api.properties_list, name='property_list'),
]