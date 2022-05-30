
# 1. --------0+++++++++5------------8+++++++++11------
#2. +++++++++0---------5++++++++++++8---------11++++++
                                        #by development NurdiansyahR
inputUser = float(input("masukan angka yang bernilai kurang dari 5 , kurang dari 8 : "))
angka1 = (inputUser > 0 and inputUser < 5)
print("kurang dari 5 = ",angka1)
angka2 = (inputUser  > 8 and inputUser < 11)
print("lebih dari 8 = ",angka2)

isCorrect  = angka1 or angka2

print("menggabungkan nilai komparasi range lebih dari 0 kurang dari 5 dan lebih dari 8 kurang dari 11 :  ",isCorrect)

inputUser = float(input("masukan angka yang bernilai kurang dari 0 , lebih dari 5 dan lebih besar dari 11 : "))

angka1 = (inputUser < 0)
angka2 = (inputUser > 5 and inputUser < 8 )
angka3 = (inputUser > 11)
isCorrect = angka1 or angka2 or angka3
print("kurang dari 0 :",angka1)
print("lebih dari 5, kurang dari 8 , lebih dari 11 :",angka2)
print("lebih dari 11 :",angka3)

print("menggabungkan nilai komparasi range kurang dari 0 lebih dari 5 \n kurang dari 8 lebih dari 11 adalah : ",isCorrect)