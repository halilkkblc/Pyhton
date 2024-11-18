cars = ["Ferrari", "Aston Martin", "Porsche"]
colors = ["Red", "Blue", "Black"]
years = [2020, 2018, 2019]

zipped_object = zip(cars, colors, years)
zipped = list(zipped_object)
print(f"zip nesnesi: {zipped_object}")
print(f"zip sonrası: {zipped}")

print("*" * 50)

unzipped_object = zip(*zipped)
unzipped = tuple(unzipped_object)
print(f'unzipped nesnesi: {unzipped_object}')
print(f'unzipped sonrası: {unzipped}')
