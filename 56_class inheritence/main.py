class Ojek():
    def __init__(self,in_name,in_transmisi,in_lokasi):
        self.name = in_name
        self.transmisi = in_transmisi
        self.lokasi = in_lokasi

    def check_id(self):
        print("nama = ",self.name,"\ntransmisi = ",self.transmisi,"\nlokasi =",self.lokasi)

class gojek(Ojek): # merupakan konsep inheritence
    def no_id(self,in_id):
        self.id = in_id
        print("id = ",self.id)
ojek1 = Ojek("nurdin","manual","bandung")
ojek2 = gojek("ahmad","automatic","bandung")

ojek1.check_id()
print(30*"-")
ojek2.check_id()
ojek2.no_id("19111012")