def test():
    print("-" * 30)
    x = 10
    print(f"test fonksiyonunun local'i: {locals()}")
    print(f"test fonksiyonunun local'i: {locals()["x"]}")


name = "haliş"

print("-" * 30)
print(f"global kapsamın local'i: {locals()}")
test()
