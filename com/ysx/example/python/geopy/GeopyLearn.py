from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="test_ysx")

names = ['天安门', '雁栖湖', '清华大学']

for name in names:
    loc = geolocator.geocode(name)
    print(name, loc.latitude, loc.longitude)
