cities = [
    ("Istanbul", 25),
    ("Izmir", 30),
    ("Mugla", 32),
    ("Antalya", 90)
]


def c_to_f(temp):
    f = (temp * (9/5)) + 32
    return f


cities_f = []
for i in cities:
    result = (i[0], c_to_f(i[1]))
    cities_f.append(result)

print(f"Fahrenheit: {cities_f}")
