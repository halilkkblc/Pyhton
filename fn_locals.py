def test():
    print("-" * 30)
    print(f"test fonksiyonunun local'i: {locals()}")


name = "haliş"

print("-" * 30)
print(f"global kapsamın local'i: {locals()}")
test()
