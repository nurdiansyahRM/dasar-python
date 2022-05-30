# tipe data
# tipe data angka atau di sebut integer
from lib2to3.pytree import type_repr
from ctypes import c_double

data_integer = 1

print ("data : ",data_integer)
print ("bertipe : ",type(data_integer))


#tipe data desimal : float

data_float =  1.2
print ("data : ",data_float)
print ("bertipe : ",type(data_float))
#kumpulan karakter
nama  = "nurdiansyah"
print ("data : ", nama)
print ("bertipe : ",type(nama))

#tipe data biner (boolean)

i = True
print ("data : ", i)
print ("bertipe : ",type(i))
 #tipe data khusus
#  bilangan komplek
data_complex = complex(5,6)
print ("data : ", data_complex)
print ("bertipe : ",type(data_complex))

#tipe data dari bahasa c

data_c_double = c_double(10.5)
print ("data : ", data_c_double)
print ("bertipe : ",type(data_c_double))
