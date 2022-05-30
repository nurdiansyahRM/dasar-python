# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5
print("nilai a = ",a)

a += 1 #artinya operator ini menambahkan angka 1 kedalam variabel a = a  + 1
print("nilai a += 1  nilai nya menjadi : ",a)

a -= 2 #artinya a = a - 2
print("nilai a -= 2 nilai nya menjadi : ",a)

a *= 5 #artinya a = a * 5
print("nilai a *= 5 nilai nya menjadi : ",a)

a /= 4 #artinya a = a / 4
print("nilai a /= 4 nilai nya menjadi : ",a)

b = 10
print("\nnilai b = ",b)

b %= 3
print("nilai b %= 3 nilai nya menjadi : ",b)



b = 10
print("\nnilai b = ",b)

b //= 3
print("nilai b /= 3 nilai nya menjadi : ",b)

a = 5
print("nilai a = ",a)

a **= 3
print("nilai a **= 3 nilai nya menjadi : ",a)

# operasi bitwase
# OR
print("========= OR ===========")
c = True
print("\nnilai c = ",c)
c |= False
print("nilai c |= False nilai nya menjadi : ",c)
c = False
print("\nnilai c = ",c)
c |= False
print("nilai c |= False nilai nya menjadi : ",c)

# AND
print("========= And ===========")

c = True
print("\nnilai c = ",c)
c &= False
print("nilai c &= False nilai nya menjadi : ",c)
c = False
print("\nnilai c = ",c)
c &= False
print("nilai c &= False nilai nya menjadi : ",c)

#XOR
print("========= XOR ===========")

c = True
print("\nnilai c = ",c)
c ^= False
print("nilai c ^= False nilai nya menjadi : ",c)
c = False
print("\nnilai c = ",c)
c ^= False
print("nilai c ^= False nilai nya menjadi : ",c)


#geser geser

d = 0b0100
print("\nnilai d = ",d )
print("nilai : ",d, 'binary : ',format(d,'04b'))
d >>= 1
print("nilai : ",d, 'binary : ',format(d,'4b'))

c = 0b1000
print("\nnilai c = ",c )
c <<= 1
print("nilai : ",c, 'binary : ',format(c,'04b'))


