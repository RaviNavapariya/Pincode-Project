from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AddressForm
import requests
import json
from .models import Address
from geopy.geocoders import Nominatim

def NewView(request):
    return render(request, 'other.html')

def PincodeView(request):
    if request.method == "POST":        
        endpoint = "https://api.postalpincode.in/pincode/"
        pincode = request.POST['pincode']
        geolocator = Nominatim(user_agent="geoapiExercises")
        zipcode = pincode
        location = geolocator.geocode(zipcode)
        address_description = location.address        
        url = endpoint+pincode
        response = requests.get(url)
        data = json.loads(response.text)
        try:
            final_data = data[0]['PostOffice']
            for i in final_data:
                district = i['District']
                state = i['State']
                country = i['Country']
        except:
            message = '<h1>Please enter valid Pincode.</h1>'
            return HttpResponse(message)
        form = AddressForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data = Address.objects.create(
                name = request.POST['name'],
                description = address_description,
                pincode = pincode,
                city = district,
                state = state,
                country = country
            )
            data.save()
            return redirect('/other/')
        pass
    else:
        form = AddressForm()
    return render(request, 'home.html', {"form":form})