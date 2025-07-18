travel_log = {
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

# Nesting lists inside other lists
nested_list = ["A", "B", ["C", "D"]]

# Getting an item that is nested deeply in a list
print(nested_list[2][1])

# Nesting a dictionary in a dictionary
travel_log_2 = {
    "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    },
}

print(travel_log_2["Germany"]["cities_visited"][2])