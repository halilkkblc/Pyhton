nums = [5, 10, 12, 7, 11]


def check_number(num):
    return num % 2 == 0


new = list(filter(check_number, nums))

filter_address = filter(check_number, nums)

print(f"çift sayilarimiz: {new}")
print(f"filter nesnemiz: {filter_address}")
