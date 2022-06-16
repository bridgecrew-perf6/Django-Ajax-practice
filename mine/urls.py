from django.urls import path,include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'hot', HotelViewset)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth',include('rest_framework.urls')),
    path('', views.hotel_image_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
    path('hotel_images', views.display_hotel_images, name = 'hotel_images'),
]