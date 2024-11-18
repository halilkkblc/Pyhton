print(globals())


def test():
    pass


name = "haliş"
globals()["soyad"] = "yexxe"

print("-" * 30)

print(globals())
print(globals()["soyad"])
print(soyad)
