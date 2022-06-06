#deep copy nested list

data_1 = [1,2]
data_2 = [3,4]

data_2D = [data_1,data_2,10]
print(f"data = {data_2D}")

#mengambil data dari nested list

data = data_2D[0][0]
print(f"data = {data}")

#data copy nested list

data_copy = data_2D.copy()
print(f"data asli = {data_2D}")
print(f"data copy = {data_copy}")

#address 
print(30*"=")
print(f"address dari data_2D = {hex(id(data_2D))}")
print(f"address dari data_copy = {hex(id(data_copy))}")
print(30*"=")
print("address dari number ke-1")
data_2D[2] = 8
print(f"data = {data_2D}")
print(f"data = {data_copy}")
print(f"address dari data_2D = {hex(id(data_2D[0]))}")
print(f"address dari data_copy = {hex(id(data_copy[0]))}")

#menggunakan deep copy

from copy import copy, deepcopy
data_2D = [data_1,data_2,10]
data_2D[0][0] = 2 
data_2D[2] = 8 
data_deepcopy = deepcopy(data_2D)
print(f"data asli = {data_2D}")
print(f"data copy = {data_copy}")
print(f"data deepcopy = {data_deepcopy}")

