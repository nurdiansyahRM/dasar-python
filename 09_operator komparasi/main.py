# operator komparasi

# setiap hasil dari operasi komparasi adalah boolean

# > ,<, >= ,<= , ==, !=, is, is not

a = 4
b = 2
# // lebih besar dari >
print("operator komparasi lebih besar dari (>) >>") 
hasil = a > b
print(a, ' > ' ,b , " = ",hasil )
# // kurang  dari >

print("operator komparasi kurang dari (<) >>") 
hasil = a < b
print(a, ' < ' ,b , " = ",hasil )

# operator komparasi lebih besar sama dengan >=
print("operator komparasi lebih besar sama dengan dari (>=) >>") 
hasil = a >= 4
print(a, ' >= ' ,4 , " = ",hasil )

# operator komparasi kurang dari sama dengan <=
print("operator komparasi kurang dari sama dengan  (<=) >>") 
hasil = a <= b
print(a, ' <= ' ,b , " = ",hasil )


# operator komparasi kurang dari sama dengan ==
print("operator komparasi sama dengan dari  (==) >>") 
hasil = a == 4
print(a, ' == ' ,4 , " = ",hasil )


# operator komparasi kurang dari sama dengan !=
print("operator komparasi tidak sama dengan dari  (!=) >>") 
hasil = a != b
print(a, ' != ' ,b , " = ",hasil )


# operator komparasi is adalah membandingkan objeck dan memory

from tkinter import Y



print("operator komparasi is object identity  (is) >>") 
x = 5 
y = 5

print("nilai x = ", x, "id = ",hex(id(x)))
print("nilai y = ", y, "id = ",hex(id(y)))

hasil = x is y
print("hasil object identity dari x dan y adalah = ", hasil)

print("operator komparasi is object identity  (is not) >>") 
x = 5 
y = 5

print("nilai x = ", x, "id = ",hex(id(x)))
print("nilai y = ", y, "id = ",hex(id(y)))

hasil = x is not y
print("hasil object identity dari x dan y adalah = ", hasil)
