list_1 = [2, 8, 16, 32, 64]


def calculate_power(num):
    return pow(num, 2)


powers = map(calculate_power, list_1)
powers_list = list(powers)

print(f"sayılarımız: {list_1}")
print(f"map objesi: {powers}")
print(f"istenen çıktı: {powers_list}")