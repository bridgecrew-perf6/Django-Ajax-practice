from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from rest_framework import viewsets
from .serializers import HotelSerializer
from .models import Hotel

# Create your views here.
def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'index.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images

def display_hotel_images(request):

	if request.method == 'GET':

		# getting all the objects of hotel.
		Hotels = Hotel.objects.all()
		return render(request, 'display.html',
					{'hotel_images' : Hotels})
  
class HotelViewset(viewsets.ModelViewSet):
    queryset =Hotel.objects.all()
    
    serializer_class =HotelSerializer

