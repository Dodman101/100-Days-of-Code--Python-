travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],        
    },
    {
        "country": "Germany", 
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],        
    },
]

#Don't change the code above

#TODO: Write the function that will allow new countries to be added to the travel log
def add_new_country(country_name, total_visits, cities_visited):
    travel_log.append({
        "country":country_name,
        "visits":total_visits,
        "cities":cities_visited
    })

#Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)