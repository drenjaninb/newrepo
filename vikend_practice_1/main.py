class Wagen:
    def start (self):
        print("Engine ON.")
    def shut_down(self):
        print("Engine Off.")

class Mazda(Wagen):
    def __init__(self,modellbezeichnung, volumen, kw, farbe):
        self.modellbezeichnung = modellbezeichnung
        self.volumen = volumen
        self.kw = kw
        self.farbe = farbe

mazdacar = Mazda(3,2000,88,'soul red')
print(mazdacar.start())

print(mazdacar.shut_down())