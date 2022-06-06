#looping dictionary

nama_mhs = {
    "nrm" :"Nurdiansyah Rizki Mubarokah",
    "alg" : "alif gufron",
    "wy" : "wiyan barkah"
}

for nama in nama_mhs :
    print(nama)
print(30*"=")
#operator untuk mengambil item/iterables

keys = nama_mhs.keys()
print(keys)
print(30*"=")

for key in nama_mhs.keys():
    print(nama_mhs.get(key))
print(30*"=")
    
value = nama_mhs.values()
print(value)
print(30*"=")

for value in nama_mhs.values():
    print(value)
print(30*"=")

items = nama_mhs.items()
print(items)

for items in nama_mhs.items():
    print(items)    
print(30*"=")

for key, value in nama_mhs.items():
    print(f"key = {key} values = {value}")
