from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
zipcode = "365430"
location = geolocator.geocode(zipcode)

print("Zipcode:",zipcode)
print("Details of the Zipcode:")
print(location)
print(location.address)
print(type(location))
print(len(location.address))


# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="geoapiExercises")
# zipcode = pincode
# location = geolocator.geocode(zipcode)
# address_description = location.address