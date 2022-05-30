# latihan logika dan komparasi

#membuat gabungan area rentang dari angka

inputUser = float(input("masukan angka yang bernilai kurang dari 3 atau lebih besar dari 10 : "))

#memeriksa angka kurang dari 3
iskurangdari = (inputUser < 3 )
print("kurang dari 3  = " ,iskurangdari)

#memeriksa angka lebih dari 10
islebihdari = (inputUser > 10)
print("lebih dari 10 = ",islebihdari)

#menggabungkan hasil dari ++++++3-----------10+++++++
isCorrect = iskurangdari or islebihdari

print("menggabungkan nilai komparasi range 3 in 10 adalah : ", isCorrect)




#case irisan
#---------3+++++++10--------
#-----3++++++++++++++
inputUser = float(input("masukan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))
islebihdari =(inputUser > 3)
print("lebih dari 3  = " ,islebihdari)
# ++++++++++++10-------------
iskurangdari = (inputUser < 10)
print("kurang  dari 10  = " ,islebihdari)
isCorrect = islebihdari and iskurangdari
print("menggabungkan nilai komparasi range 3 >< 10 adalah : ",isCorrect) 

