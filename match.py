import typing

class City(typing.NamedTuple):
    continent:str
    name:str
    country:str


cities = [
    City('Asia','Tokyo','JP'),
    City('Asia','Delhi','IN'),
    City('North America','Mexico City','MX'),
    City('North America','New York','US'),
    City('South America','São Paulo','BR'),
]

# Keyword Class Patterns

def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results
    
def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia',country=cc):
                results.append(cc)

    return results

# Positional Class Patterns

def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City("Asia",_, country):
                results.append(country)
    return results

if __name__=='__main__':
    # Print os resultados de match asian cities e countries com Keyword class pattern
    print(match_asian_cities())
    print(match_asian_countries())

    # Print os resultados de match asian cities e countries com Positional class pattern
    print(match_asian_cities_pos())
    print(match_asian_countries_pos())