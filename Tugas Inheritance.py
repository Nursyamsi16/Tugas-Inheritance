class Mobil(object):
    def jenis_kendaraan(self):
        print("jenis_kendaraan: Mobil")
    
    def __init__(self, r, t):
        self.roda = r
        self.mesin = t
        

    def cetakdata(self):
        print("roda\t:", self.roda)
        print("mesin\t:", self.mesin)


#mendefinisikan kelas turunan (subclass)
class Avanza(Mobil):
    def Tipe_Mobil (self):
        print("Avanza")
    def __init__(self, r, m, h):
        self.roda = r
        self.mesin = m
        self.harga = h

    def cetakdata(self):
        print("roda\t:",  self.roda)  
        print("mesin\t:", self.mesin)
        print("harga\t:", self.harga)

def main():
   Mobil1 = Mobil (4, 1)
   Avanza1 = Avanza (4, 1, "135 jt")
   
   Mobil1.jenis_kendaraan()
   Mobil1.cetakdata()
   Avanza1.Tipe_Mobil()
   Avanza1.cetakdata()
   
if __name__== "__main__":
    main()
