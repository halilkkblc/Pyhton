nums = [5, 10, 12, 7, 11]

temporary = filter(lambda i: i % 2 == 0, nums)
main_new = list(temporary)

print(temporary)
print(main_new)
