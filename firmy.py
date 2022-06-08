import json

class Nova_firma:
    def __init__(self, jmeno, ulice, cp, mesto, psc):
        self.jmeno = jmeno.upper()
        self.ulice = ulice.title()
        self.cislo_popisne = cp
        self.mesto = mesto.title()
        self.psc = psc
        self.adresa = f"""{self.jmeno} \n{self.ulice} {self.cislo_popisne} \n{self.mesto} \n{self.psc}"""

    def __str__(self):
        return self.jmeno

class DatabazeFirmy:
    def __init__(self):
        self.firmy = []

    def vytvorit(self):
        chyba = True

        while chyba:
            try:
                jmeno = input("Zadej název firmy:\n")
                ulice = input("Zadej ulici:\n")
                cp = input("Zadej číslo popisné:\n")
                mesto = input("Zadej město:\n")
                psc = int(input("Zadej PSČ:\n"))
                chyba = False
            except:
                print("\n!!!Vyskitla se chyba!!!\nZadejte firmu znovu\n")
        
        self.firmy.append(Nova_firma(jmeno, ulice, cp, mesto, psc))



    def ulozit(self):
        outfile = open("./data/DbFirmy.json", "w")
        data = {}
        for firma in self.firmy:
            data.setdefault(f'{firma.jmeno}', {"Nazev":f"{firma.jmeno}", "Nazev":f"{firma.jmeno}", "ulice":f"{firma.ulice}", "c.p.":f"{firma.cislo_popisne}", "mesto":f"{firma.mesto}", "psc":f"{firma.psc}"})
        json.dump(data, outfile, indent=4)
        outfile.close()



    def nacti(self):
        with open("./data/DbFirmy.json", "r") as infile:
            firmy = json.load(infile)
            for firma in firmy.values():
                self.firmy.append(Nova_firma(firma["Nazev"], firma["ulice"], firma["c.p."],firma["mesto"], firma["psc"]))
            


    def vyhledat(self):
        hledana_firma = input("Zadej název vyhledávané firmy: ")
        for firma in self.firmy:
            if hledana_firma.upper() == firma.jmeno:
                return (f"Hledaná firma je v seznamu. \n{firma.adresa}\n")
            else:
                continue
        return(f"V seznamu nebyla nalezena firma s nazvem {hledana_firma}.")
            


    def upravit(self):
        chyba = True
    
        while chyba:
            try:
                index = 0
                for firma in self.firmy:
                    index +=1
                    print(f"{index} : {firma.jmeno}")
                if index == 0:
                    print("\nDatabáze je prázdná. Nejprve načtěte databázi nebo vytvořte firmu.\n")
                    chyba = False
                    return
                volba = int(input("zadej číslo firmy pro upravu: "))
                if volba >= 1 and volba <= (index):
                    chyba = False
                else:
                    print(f"\nChybná volba\nzadejte hodnotu 1 -", (index),"\n")
                
            except:
                print("""\n!!! VYSKYTLA SE CHYBA !!! Opakujte  operaci\n""")
            
        hl_firma = (self.firmy[volba-1])
        chyba = True

        while chyba:
            try:
                for firma in self.firmy:
                    if firma == hl_firma:
                        volba = int(input(""" 0 : konec\n 1 : Název\n 2 : Ulice\n 3 : číslo popisné\n 4 : Město\n 5 : PSČ\n\nCo chceš upravit: """))
                        if volba == 0:
                            return
                        elif volba > 1 and volba < 5:
                            hodnota = input("Zadej novou hodnotu: ")
                            if volba == 1:
                                firma.jmeno = hodnota.upper()
                                chyba = False
                            elif volba == 2:
                                firma.ulice = hodnota.title()
                                chyba = False
                            elif volba == 3:
                                firma.ulice = int(hodnota)
                                chyba = False
                            elif volba == 4:
                                firma.ulice = hodnota.title()
                                chyba = False
                            elif volba == 5:
                                firma.ulice = int(hodnota)
                                chyba = False
                        else:
                            print("\nChybná hodnota volby\n")
            except:
                print("""!!! VYSKYTLA SE CHYBA !!! Opakujte operaci""")
                chyba = True



    def smazat(self):
        chyba = True
    
        while chyba:
            try:
                index = 0
                for firma in self.firmy:
                    index +=1
                    print(f"{index} : {firma.jmeno}")
                if index == 0:
                    print("\nDatabáze je prázdná.\n")
                    chyba = False
                    return
                volba = int(input("zadej číslo firmy pro upravu: "))
                if volba >= 1 and volba <= (index):
                    chyba = False
                else:
                    print(f"\nChybná volba\nzadejte hodnotu 1 -", (index),"\n")
                
            except:
                print("""\n!!! VYSKYTLA SE CHYBA !!! Opakujte  operaci\n""")

        hl_firma = (self.firmy[volba-1])

        for firma in self.firmy:
            if firma == hl_firma:
                while True:
                    volba = input(f"Opravdu chcete vymazat firmu {firma}?\n")
                    if volba.upper() == "Y":
                        self.firmy.remove(firma)
                        return
                    elif volba.upper() == "N":
                        return
                    else:
                        print("Zadaly jste nesprávnou hodnotu.")

    def __str__(self):
        vypis_firem = "\n"
        for firma in self.firmy:
            vypis_firem += f"{str(firma.jmeno)}\n" 
        return vypis_firem



dbfirem = DatabazeFirmy()
pokracovat = True

while pokracovat:
    volba = int(input("1: načti databázi firem\n2: vytvořit firmu\n3: upravit firmu\n4: smazat firmu\n5: vypiš firmy\n6: vyhledat firmu\n7: uložit\n\n 0: konec programu\n\nTvá volba: "))

    if volba == 0:
        exit()
    elif volba == 1:
        dbfirem.nacti()
    elif volba == 2:
        dbfirem.vytvorit()
    elif volba == 3:
        dbfirem.upravit()
    elif volba == 4:
        dbfirem.smazat()
    elif volba == 5:
        print(dbfirem)
    elif volba == 6:
        print(dbfirem.vyhledat())
    elif volba == 7:
        dbfirem.ulozit()
    else:
        print("\n!!! Chybná volba !!!\n")
    