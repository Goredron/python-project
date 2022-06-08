import datetime


x = datetime.datetime.now()

y = datetime.datetime(2022 , 3 , 2)

print(f"aktualní datum je: {x}")
print(f"datum zplatnosti je: {y}")

if(x > y):
    a = x - y
    print(f"Faktura je po splatnosti {a}")

else:
    a = y - x
    print(f"do splatnosti zbýva ještě {a}")


datum_vystaveni = ""

if datum_vystaveni == "":
    datum_vystaveni = datetime.datetime.today()
    datum_splatnosti = datum_vystaveni + datetime.timedelta(days=14)

# print(datum_vystaveni)
# print(datum_splatnosti)



