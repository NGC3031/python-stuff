''' City Function for unit testing - t e s t'''


def city_function(city="Sydney", country="Australia"):
    tmp = city.capitalize()+", " + country.capitalize()
    print(tmp)
    return tmp
