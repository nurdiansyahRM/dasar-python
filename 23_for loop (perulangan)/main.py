# perulangan (loop)

# for kondisi : 
#     aksi
# 1. list
angka_list =[0,1,2,3,4] #ini adalah list
# print(angka_list)
for i in angka_list:
    print(f"i sekarang -> {i}")

print("this is end program 1 \n")

# 2. range
angka_range = range(5)
for i in angka_range:
    print(f"{i}.aku ganteng")
    
print("this is end program 2\n")

for i in range(3) :
    print(f"{i}.aku ganteng")

print("this is end program 3 \n")

# 3. bisa loop using str
data_str  = "aku keren sekali"
for i in data_str:
    print(i)

print("this is end program 4")