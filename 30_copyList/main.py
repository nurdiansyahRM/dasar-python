# teknik menduplikat list
#teknik copy by reference 
data_1 = ["nurdin","ahmad","jojo","rendi"]
data_2 = data_1
print(f"data_1 -> {data_1}") 
print(f"data_2 -> {data_2}") 

print(40*"=")

data_2.sort()
print(f"data_1 -> {data_1}") 
print(f"data_2 -> {data_2}") 

print(40*"=")

data_2[0] = "ucup"

print(f"data_1 -> {data_1}") 
print(f"data_2 -> {data_2}") 
print(40*"=")

print(f"address data_1 -> {hex(id(data_1))}")
print(f"address data_2 -> {hex(id(data_2))}")
 
 #teknik copy by duplicate using copy()
 
data_3 = data_1.copy()

print(40*"=")
print(f"address data_1 -> {hex(id(data_1))}")
print(f"address data_2 -> {hex(id(data_2))}")
print(f"address data_3 -> {hex(id(data_3))}")# address ya berbeda dengan data_1 dan data_2
print(40*"=")

data_3[1] = "nurdin"
print(f"data_1 -> {data_1}") 
print(f"data_2 -> {data_2}") 
print(f"data_3 -> {data_3}") 


