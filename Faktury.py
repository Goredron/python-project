import datetime

faktury = []



class Faktura:
    def __init__(self, faktura, odesilatel, prijemce, splatnost, popis, cena):
        self.cislo_faktury = faktura
        self.odesilatel = odesilatel
        self.prijemce = prijemce
        self.datum_vystaveni = datetime.datetime.today()
        self.datum_splatnosti = self.datum_vystaveni + datetime.timedelta(days=splatnost)
        self.popis = popis
        self.cena = cena

    def __str__(self):
        return self.cislo_faktury

faktura = Faktura("22FA-001", "Luboš Krameš", "Gating services a.s.", 14, "gfagfsdg", "30.000kč")


print (faktura)