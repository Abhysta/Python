# dalam python semuanya berbentuk dasar objek baik string, int, list, dll
# class digunakan untuk memodelkan atau mengkarakteristikan suatu objek
# penulisan class diawali dengan class nama kelas: yang kemudian diawali dengan blok kode def atau def disini
# disebut juga method yang kemudian diawali __init__ untuk inisiasi nilai awal atau atribut yang akan dimasukkan
# pada method pada class dan __init__(self), self dimaksudkan untuk mengacu pada objek dalam kelas yang didefinisikan
# misal class kotak maka self akan mengacu pada kotak
# contoh
class segitiga:
    def __init__(self):
        self.alas = 0
        self.tinggi = 0

#untuk memanggil kelas dapat digunakan 
obj = segitiga()
obj.alas = 5
obj.tinggi = 10
luas = (obj.alas * obj.tinggi) / 2
print(luas)

#contoh dengan parameter
class segitiga2:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

#untuk memanggil kelas dapat digunakan 
obj2 = segitiga2(5, 10)
luas2 = (obj2.alas * obj2.tinggi) / 2
print(luas2)

# untuk mendefinisikan method lain pada class dapat dilakukan penamaan seperti pada fungsi biasanya, 
# gunakan self untuk memanggil nilai dri method awal
#contoh dengan method baru
class segitiga3:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    def cetakluas(self):
        print((self.alas * self.tinggi) / 2)

#untuk memanggil kelas dapat digunakan 
obj3 = segitiga3(5, 10)
print(obj3.luas())
obj3.cetakluas()

#atribut statis, umumnya nilai dari objek sebuah class berbeda-beda namun bisa disamakan dengan menggunakan
#atribut statis atau atrubut tetap, penulisan atribut statis dilakukan sebelum pendefinisian method
#nilai statis dapat diakses dengan menggunakan nama kelas
class segitiga4:
    #atribut statis
    objectCount = 0

    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

        #menaikan nilai atribut statis
        segitiga4.objectCount += 1
    
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    def cetakluas(self):
        print((self.alas * self.tinggi) / 2)

#untuk memanggil kelas dapat digunakan 
obj4 = segitiga4(5, 10)
obj5 = segitiga4(5, 10)
obj6 = segitiga4(5, 10)
print(segitiga4.objectCount)

# selain atribut statis terdapat juga method statis untuk mendefinisikan method statis diawali dengan
# @staticmethod dan tidak perlu self untuk pendefinisian atributnya
class segitiga5:
    #atribut statis
    objectCount = 0

    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

        #menaikan nilai atribut statis
        segitiga4.objectCount += 1
    
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    @staticmethod
    def daftarAtribut():
        return ('alas', 'tinggi')
    
    def cetakluas(self):
        print((self.alas * self.tinggi) / 2)

#untuk memanggil method statis dapat digunakan 
print(segitiga5.daftarAtribut())

#properti, yaitu method yang nilainya hanya akan diakses jika dipanggil
# penulisan properti dengan @property
class segitiga6:
    #atribut statis
    objectCount = 0

    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

        #menaikan nilai atribut statis
        segitiga4.objectCount += 1
    
    @property
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    @staticmethod
    def daftarAtribut():
        return ('alas', 'tinggi')
    
    def cetakluas(self):
        print((self.alas * self.tinggi) / 2)

#untuk memanggil property dapat digunakan 
obj7 = segitiga6(5,5)
print(obj7.luas)

#methode private, yaitu untuk mendifinisikan method yang hanya bisa diakses di dalam class
#untuk pendefinisian method private dapat diawali dengan __namamthod
class segitiga7:
    #atribut statis
    objectCount = 0

    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

        #menaikan nilai atribut statis
        segitiga4.objectCount += 1
    
    def __luas(self):
        return (self.alas * self.tinggi) / 2
    
    @staticmethod
    def daftarAtribut():
        return ('alas', 'tinggi')
    
    def cetakluas(self):
        print((self.alas * self.tinggi) / 2)

#untuk memanggil property dapat digunakan 
obj8 = segitiga7(5,5)
print(obj8.cetakluas())
# print(obj8.luas()) #error

#kelas turunan, seperti bahasa pemrograman lain class dalam python juga dapat diturunkan caranya dengan
#class namakelasturunan(namakelasinduk)
#dan untuk memanggil atribut dalam kelas induk dapat menggunakan super()
class turunanSegitiga(segitiga7):
    def __init__(self, a, t):
        super().__init__(a, t)
    
    def tes(self):
        import math
        return math.sqrt((self.alas**2) + (self.tinggi**2))
    
obj9 = turunanSegitiga(5,6)
print(obj9.tes())

#turunan jamak
class alas():
    def __init__(self, a):
        self.alas = a
    
class tinggi():
    def __init__(self, t):
        self.tinggi = t

class turunanJamak(alas, tinggi):
    def __init__(self, a, t):
        alas.__init__(self, a)        
        tinggi.__init__(self, t)    

    def luas(self):
        return (self.alas * self.tinggi) / 2

obj10 = turunanJamak(2,3)
print(obj10.luas())    