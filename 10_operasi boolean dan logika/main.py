#operasi logika atau boolean

# not , or, and, xor

from ast import Or
from operator import xor


print("====== NOT ======")
a = True
c = not a
print("data a = ",a)
print("--------------NOT")
print("data c = ",c)


print("====== OR ======")
a = True
b = False
c = a or b
print(a, ' OR ' ,b , '=',c)

a = False
b = True
c = a or b
print(a, ' OR ' ,b , '=',c)

a = True
b = True
c = a or b
print(a, ' OR ' ,b , '=',c)

a = False
b = False
c = a or b
print(a, ' OR ' ,b , '=',c)


print("====== AND ======")
a = True
b = False
c = a and b
print(a, 'OR' , b,'=',c)

a = False
b = True
c = a and b
print(a, ' and ' ,b , '=',c)

a = True
b = True
c = a and b
print(a, ' and ' ,b , '=',c)

a = False
b = False
c = a and b
print(a, ' and ' ,b , '=',c)

print("====== Xor ======")
a = True
b = False
c = a ^ b
print(a, 'Xor' , b,'=',c)

a = False
b = True
c = a ^ b
print(a, ' Xor ' ,b , '=',c)

a = True
b = True
c = a ^ b
print(a, ' Xor ' ,b , '=',c)

a = False
b = False
c = a ^ b
print(a, ' Xor ' ,b , '=',c)
