# latihan perulangan membuat segitiga
print(15*"=" + "For" + 15*"=")
sisi = 10
count = 1
for i in range (sisi) : 
    # for i in range(sisi_2):
    print("*"*count)
    count += 1
print("=" * 35)

# 2. using while kondisi

print(15*"=" + "while" + 15*"=")
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break;
    
print("=" * 35)
print("=" * 35)
count = 1
while True:
    if (count % 2 == 1):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print("this end the program")        
print("=" * 35)

print("=" * 35)
count = 1
spasi = int(sisi/2)

while True:
    if(count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count +=1
        continue
    
    if (count > sisi):
        break
count = 10
sisi = 1
spasi = 1
while True :
    if count %2:
        print(" "*spasi,"+"*count)
        spasi +=1
        count -=1
    else:
        count-=1
        continue
    if(count < sisi):
        break
        


print("this end the program")
print("=" * 35)