# operator bitwise
a  = 9
b = 5

# bitwase or (|)
c = a | b
print("\n========= OR =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("nilai : ",b, 'binary : ',format(b,'08b'))
print("---------------------------(|)")
print("nilai : ",c, 'binary : ',format(c,'08b'))

# bitwase (and)
c = a & b
print("\n========= And =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("nilai : ",b, 'binary : ',format(b,'08b'))
print("---------------------------(&)")
print("nilai : ",c, 'binary : ',format(c,'08b'))

# bitwase (Xor)
c = a ^ b

print("\n========= Xor =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("nilai : ",b, 'binary : ',format(b,'08b'))
print("---------------------------(^)")
print("nilai : ",c, 'binary : ',format(c,'08b'))

c = ~ a
print("\n========= Not =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("---------------------------(~)")
print("nilai : ",c, 'binary : ',format(c,'08b'))
print("---------------------------(^)")
d = 0b0000001001
e = 0b1111111111
print("nilai : ",e^d,', binary :',format(e^d,'08b'))

#shifting

#shift right
c = a >> 1
print("\n========= Shiftright =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("nilai : ",b, 'binary : ',format(b,'08b'))
print("---------------------------(>>)")
print("nilai : ",c, 'binary : ',format(c,'08b'))

#shift left
c = a << 1
print("\n========= Shiftleft =========")
print("nilai : ",a, 'binary : ',format(a,'08b'))
print("nilai : ",b, 'binary : ',format(b,'08b'))
print("---------------------------(<<)")
print("nilai : ",c, 'binary : ',format(c,'08b'))
