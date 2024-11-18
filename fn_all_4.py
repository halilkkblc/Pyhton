name_1 = input("Lutfen birinci kisinin adini giriniz: ")
name_2 = input("Lutfen ikinci kisinin adini giriniz: ")

a = [name_1.strip(), name_2.strip()]
if all(a):
    print("Bilgiler girildi")
else:
    print("Bilgiler girilmedi")
