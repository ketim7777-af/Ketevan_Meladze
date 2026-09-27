
location = [("Tbilisi", 41.71, 44.82), ("Batumi", 41.64, 41.63), ("Kutaisi", 42.26, 42.71)]
for city, latitude, longitude in location:
    print(f"City: {city}, Latitude: {latitude:.2f}, Longitude: {longitude:.3f}")

city_names = [city for city, latitude,longitude in location]
print(city_names)
    
