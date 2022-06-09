from collections import deque
import os

os.system("cls")
def lines():
    print(40*"-")
    
#ini merupakan teknik stack
tumpukan =[1,2,5,7,9]
tumpukan.append(5)
print(f"data yang di tambah -> ",9)
lines()
print(f"data sekarang -> :{tumpukan}")
lines()
out = tumpukan.pop()
print(f"data keluar -> {out}")
lines()
print(f"data sekarang -> :{tumpukan}")

#teknik queues
print("\n")
print(20*"-","queues",20*"-")
antrian = deque([1,4,8,9,5])
print('data sekarang : ',antrian)
#menambah data 
antrian.append(6)
print("data masuk adalah -> ",6)
lines()
print('data sekarang : ',antrian)
antrian.append(7)
print("data masuk adalah -> ",7)
lines()
print('data sekarang : ',antrian)

#mengurangi antrian


out = antrian.popleft();
print(f"data keluar -> {out}")