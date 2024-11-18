cities = [
    ("Istanbul", 25),
    ("Izmir", 30),
    ("Muğla", 32),
    ("Antalya", 90)
]

c_to_f = lambda city: (city[0], (city[1] * (9/5)) + 32)

cities_f = list(map(c_to_f, cities))

print(f"adresi: {c_to_f}")
print(f"Fahrenheit: {cities_f}")
