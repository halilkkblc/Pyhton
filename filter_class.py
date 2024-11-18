nums = [5, 10, 12, 7, 11]
new = []


def check_number(num):
    return num % 2 == 0


for i in nums:
    result = check_number(i)
    if result:   # (if result == True:) yazmamıza gerek yok
        new.append(i)

print(f"çift sayilarimiz: {new}")
