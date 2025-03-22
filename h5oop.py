class Hesap:
    def _init_(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2 

    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def sonuc(self):
        return {
            "Toplam": self.topla(),
            "Fark": self.cikar(),
            "Çarpım": self.carp()
        }


hesaplama = Hesap(5, 4)
print("Toplam:", hesaplama.topla()) 
print("Çıkarma:", hesaplama.cikar())  
print("Çarpma:", hesaplama.carp())  
print("Sonuçlar:", hesaplama.sonuc())