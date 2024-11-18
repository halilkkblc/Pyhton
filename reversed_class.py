list_1 = [10, 20, 30, 40, 50]
r = reversed(list_1)

print(f'tipi: {type(r)}')  # iterator
print(f'iterator adresi: {r}')  # object(nesne) değil
print(list(r))
print(list_1)
