# Import Nominatim from geocoders of geopy module using the import keyword 
from geopy.geocoders import Nominatim
# Create an object for Nominatim() class by passing some random user_agent as an argument to it.
# Here user_agent is the app name to which it is provides services.
location = Nominatim(user_agent= "GetLocationdetails")

# Pass some random location to the geocode() function and apply it on the above location(Nominatim)
# Here it gives geopy.location.Location object which contains the address and the coordinate
Locationinfo = location.geocode("Mumbai Maharastra")
# Get the address of the above given location using the address attribute
print("Address = ", Locationinfo.address)
# Get the latitude of the above given location using the latitude attribute
print("Latitude = ", Locationinfo.latitude)
# Get the longitude of the above given location using the longitude attribute
print("Longitude = ", Locationinfo.longitude)
# Get the altitude of the above given location using the altitude attribute
print("Altitude = ", Locationinfo.altitude)