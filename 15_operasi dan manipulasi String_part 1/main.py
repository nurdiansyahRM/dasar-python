# operasi dan manipulasi String

from tokenize import String
from typing import Concatenate


# 1. penyambungan String (Concatenate)

first_name = "nurdianyah"
middle_name= "Rizki"
end_name = "Mubarokah"

full_name = first_name +" "+ middle_name +" "+ end_name
print("full name : " ,full_name)

# 2. menghitung panjang dari String

panjang = len(full_name)
print("panjang dari nama ", full_name , "adalah : ", panjang)

# 3. operator untuk String

# mengecek apakah ada komponen char atau String di String

status  = "a" in full_name
print("apakah ada huruf 'a' di nama "+ full_name + ' : '+ str(status))

d = 'N'
status  = d not in full_name
print("apakah tidak ada huruf " + d + " di "+  full_name + ' : '+ str(status))


# mengulang String
print("wk" *10)

# indexing

print("index ke - 0 : " +full_name[0])
print("index ke - (-1) : " +full_name[-1])


# range
print("index ke-[0,2,4,6,8,10] : "+ full_name[0:10:2])

# item paling kecil
print("paling kecil : ", min(full_name))
print("paling besar : ", max(full_name))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count('o')
print('jumlah o pada ' + data + " = " + str(jumlah))

