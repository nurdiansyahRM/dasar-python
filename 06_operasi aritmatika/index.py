# operasi aritmatika

# operasi pertambahan
a = 10
b = 3
hasil = a + b
print('1. ',a ,' + ',b , '=' ,hasil)

# operasi pengurangan
hasil = a - b
print('2. ' ,a ,' - ',b , '=' ,hasil)

# operasi perkalian
hasil = a * b
print('3. ',a ,' * ',b , '=' ,hasil)

# operasi pembagian
hasil = a / b
print('4. ',a ,' / ',b , '=' ,hasil)

# operasi modulus (sisa bagi)
hasil = a % b

print('5. ',a ,' % ',b , '=' ,hasil)

# operasi ekspononen (pangkat)

hasil = a ** b
print('6. ',a ,' ** ',b , '=' ,hasil)

# operasi floor division

hasil = a // b
print('7. ',a ,' // ',b , '=' ,hasil)


# prioritas operasi, operasi precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print('7. ',x ,' ** ', y,  ' * ',z,' + ' ,x, ' / ',y, ' - ', y , '%', z ,'//', x,'=' ,hasil)


'''
1. ()
2. eksponen **
3. perkalian dan teman-teman * /  // %
4. pertambahan dan pengurangan + - 
'''