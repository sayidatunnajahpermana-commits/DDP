import math

def Lpersegi (sisi):
    return sisi * sisi

def Lsegitiga (alas, tinggi):
    return 0.5 * alas * tinggi

def Llingkaran (jari_jari):
    return 3.14 * jari_jari * jari_jari

def Ljajar_genjang (alas, tinggi):
    return alas * tinggi

def Lpersegi_panjang (panjang, Lebar):
    return panjang * Lebar              

print(Lpersegi_panjang(5,9))
print(Lsegitiga(4,6))
print(Llingkaran(10))
print(Ljajar_genjang(7,5))
print(Lpersegi_panjang(3,8))


def Kpersegi (sisi):
    return 4 * sisi

def Ksegitiga (sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def Klingkaran (jari_jari):
    return 2 * 3.14 * jari_jari

def Kjajaran_genjang (sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

def Kpersegi_panjang (panjang, Lebar):
    return 2 * (panjang+Lebar)
                
print()                
print(Kpersegi(5))
print(Ksegitiga(8,5,4))
print(Klingkaran(14))
print(Kjajaran_genjang(9,5))
print(Kpersegi_panjang(6,3))