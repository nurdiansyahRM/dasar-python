# kumpulan loop dalam list

# for loop
kumpulan_angka = [1,3,3,4,5,6,7,8,9]
print(f"data list -> {kumpulan_angka}")
print(30*"=")

panjang =len(kumpulan_angka) 
for angka in range (panjang):
    print(angka +1 ,f" angka = {kumpulan_angka[angka]}" )
    
nama_orang = ["ucup","ahmad","sobar"]

panjang = len(nama_orang)
for i in range(panjang):
    print(i+1,f" nama -> {nama_orang[i]}")
    
    # for loop dan range
    
kumpulan_angka = [1,3,3,4,5,6,7,8,9,2]

panjang = len(kumpulan_angka)
print(30*"=")

for i in range(panjang):
    print(i+1,f"angka = {kumpulan_angka[i]}")
print(30*"=")
    
 #while loop
i = 0
while i < panjang:
    print(f"{i+1}. angka = {kumpulan_angka[i]}")     
    i += 1
print(30*"=")
#list comprehension

data =["alif",1,2,3,"ahmad"]
[print(f"data = {i}") for i in data]
print(30*"=")

#enumate
data_list =["alif",1,2,3,"rojak","ahmad"]
for index,data in enumerate (data_list):
    print(f"index = {index}, data = {data}")