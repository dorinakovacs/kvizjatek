# 1 MEGENGEDŐ STR

# def egyszerusit(szoveg):
   # return szoveg.strip().lower().replace("á", "a")\
    #    .replace("é", "e")\
     #   .replace("í", "i")\
      #  .replace("ö", "o")\
       # .replace("ó", "o")\
        #.replace("ő", "o")\
        #.replace("ú", "u")\
        #.replace("ű", "u")\
        #.replace("ü", "u")
print("Üdvözöllek a kvízjátékban! Minden jó válasz 1 pontot ér. Vigyázz! ")
print("Ha egy kérdésre nem megfelelő típusú választ adtál, a játék átugrik a következő blokkra, és értékes pontokat veszíthetsz!"
      "Jó szórakozást!")

import unidecode
from difflib import SequenceMatcher
pontszam = 0
kerdesek_szama = 0

def egyszerusit(szoveg):
    return unidecode.unidecode(szoveg.strip().lower())

valasz = input("Mi Olaszország fővárosa?")
helyes_valasz = "Róma"
kerdesek_szama += 1

if egyszerusit(valasz) == egyszerusit(helyes_valasz):
    print("A válasz helyes!")
    pontszam += 1
elif SequenceMatcher(None, valasz, helyes_valasz).ratio() >= 0.75:
    print(f"A válasz majdnem helyes, a teljesen helyes {helyes_valasz} lett volna")
else:
    print(f"A válasz helytelen, a helyes válasz {helyes_valasz} lett volna!")


helyes_valasz = 9.8
tolerancia = 0.04

while True:
    try:
       valasz = float(input("Mekkora a gravitációs gyorsulás értéke? [m/s2] "))
       valaszszam = int(valasz)
       break
    except Exception as e:
        print('Hiba történt: ' +str(e))

kerdesek_szama += 1
if helyes_valasz - tolerancia < valasz < helyes_valasz + tolerancia:
    print("A válasz helyes!")
    pontszam += 1
else:
    print("A válasz helytelen, a helyes válasz ", helyes_valasz, " lett volna")


import random

országok_fővárosai = {
    'Albánia': 'Tirana',
    'Andorra': 'Andorra la Vella',
    'Ausztria': 'Bécs',
    'Belgium': 'Brüsszel',
    'Bosznia-Hercegovina': 'Szarajevó',
    'Bulgária': 'Szófia',
    'Csehország': 'Prága',
    'Dánia': 'Koppenhága',
    'Egyesült Királyság': 'London',
    'Észtország': 'Tallinn',
    'Fehéroroszország': 'Minszk',
    'Finnország': 'Helsinki',
    'Franciaország': 'Párizs',
    'Görögország': 'Athén',
    'Hollandia': 'Amszterdam',
    'Horvátország': 'Zágráb',
    'Írország': 'Dublin',
    'Izland': 'Reykjavík',
    'Lengyelország': 'Varsó',
    'Lettország': 'Riga',
    'Liechtenstein': 'Vaduz',
    'Litvánia': 'Vilnius',
    'Luxemburg': 'Luxembourg',
    'Észak-Macedónia': 'Szkopje',
    'Magyarország': 'Budapest',
    'Málta': 'Valletta',
    'Moldova': 'Chișinău',
    'Monaco': 'Monaco',
    'Montenegró': 'Podgorica',
    'Németország': 'Berlin',
    'Norvégia': 'Oslo',
    'Portugália': 'Lisszabon',
    'Románia': 'Bukarest',
    'Olaszország': 'Róma',
    'Oroszország': 'Moszkva',
    'San Marino': 'San Marino',
    'Svédország': 'Stockholm',
    'Svájc': 'Bern',
    'Szerbia': 'Belgrád',
    'Szlovákia': 'Pozsony',
    'Szlovénia': 'Ljubljana',
    'Spanyolország': 'Madrid',
    'Törökország': 'Ankara',
    'Ukrajna': 'Kijev',
    'Vatikán': 'Vatikán',
}

kerdesekszama = 5
valaszlehetosegek_szama = 4

try:
    for orszag in (random.sample(list(országok_fővárosai.keys()), kerdesekszama)):
            helyes_valasz = országok_fővárosai[orszag]
            helytelen_valaszok = list(országok_fővárosai.values())
            helytelen_valaszok.remove(helyes_valasz)
            kivalasztott_fovarosok = random.sample(helytelen_valaszok, 3)
            kivalasztott_fovarosok.append(helyes_valasz)
            random.shuffle(kivalasztott_fovarosok)
            kivalasztott_fovarosok_szotar = {chr(ord("A") + i): kivalasztott_fovarosok[i] for i in
                                             range(valaszlehetosegek_szama)}

            print("Mi " + orszag + " fővárosa?")
            for betu, fovaros in kivalasztott_fovarosok_szotar.items():
                print("     " + betu + "." + fovaros)
            valasz = str(input(" »"))
            valasz_fovaros = kivalasztott_fovarosok_szotar[valasz.upper()]
            if valasz_fovaros == helyes_valasz:
                print("A válasz helyes!")
                pontszam += 1
            else:
                print("A válasz helytelen! A helyes válasz " + helyes_valasz + " lett volna")

except Exception as e:
    print('Hiba történt: ' +str(e)+ 'ugrás a következő blokkra!')

kerdesek_szama += 5


csoki_fajtak = { "kerek", "szögletes", "hosszú", "rövid", "gömbölyű", "lapos", "tömör", "lyukas",
                 "csomagolt", "meztelen", "egész", "megkezdett", "édes", "keserű", "csöves",
                 "mogyorós", "tej", "likőrös", "tavalyi", "idei",}

print("Milyen fajta csokit szeret Gombóc Artúr?")
beirt_csoki_fajtak = set()

while True:

    csokolade = input("Csokoládé fajta (vagy vége):")
    if csokolade == "vége":
        break
    elif csokolade == "":
        continue
    elif csokolade in beirt_csoki_fajtak:
        print("Ez már volt!")
    elif csokolade in csoki_fajtak:
        print("Helyes válasz")

    else:
        print("Téves!")
    beirt_csoki_fajtak.add(csokolade)

eltalalt_csokik = csoki_fajtak.intersection(beirt_csoki_fajtak)

talalati_arany = len(eltalalt_csokik)/len(csoki_fajtak)*100
if talalati_arany == 100:
    pontszam += len(csoki_fajtak)
elif talalati_arany >= 80:
    pontszam += 5
elif talalati_arany >= 50:
    pontszam += 3
else:
    pontszam += 0

kerdesek_szama = kerdesek_szama + len(beirt_csoki_fajtak)

eltalalt_csokik = csoki_fajtak.intersection(beirt_csoki_fajtak)
print("Eltalált csoki fajták:" + ",".join(eltalalt_csokik))
print("Találati arány:" +str(len(eltalalt_csokik)/len(csoki_fajtak)*100)+ "%")
print("Kimaradt: " +",".join(csoki_fajtak.difference(beirt_csoki_fajtak)))
print("Hibás tippek: " + ",".join(beirt_csoki_fajtak.difference(csoki_fajtak)))



while True:
    try:
       valasz_str = input("Melyik évben vezették be a Gergely-naptárt?")
       valasz_szam = int(valasz_str)
       break
    except Exception as e:
        print('Hiba történt: ' +str(e))

kerdesek_szama += 1
helyes_valasz = 1582

elteres_szam = valasz_szam - helyes_valasz
if elteres_szam == 0:
    pontszam += 1
else:
    pontszam += 0

elteres_str = str(elteres_szam)
print('Eltérés: ' +elteres_str+ ' év')


import datetime

kerdesek = [
    ('Mikor született Petőfi Sándor?', '1823-01-01'),
    ('Mikor történt az első Holdraszállás?', '1969-07-20'),
    ('Mikor kiáltották ki Magyarországon a mai köztársaságot?', '1989-10-23'),
    ('Mikor lett Magyarország az EU tagja?', '2004-05-01')
]

print('A válaszokat ÉÉÉÉ-HH-NN formában add meg!')

try:
    for kerdes, helyesvalasz in kerdesek:
        kerdesek_szama += 1
        valasz = input(kerdes)
        valasz_datum = datetime.date.fromisoformat(valasz)
        helyesvalasz_datum = datetime.date.fromisoformat(helyesvalasz)
        elteres_napok = (valasz_datum - helyesvalasz_datum).days
        if elteres_napok == 0:
            print('A válasz helyes!')
            pontszam += 1
        else:
            print(f'A válasz helytelen, a helyes válasz {helyesvalasz} lett volna. Eltérés: {elteres_napok} nap')

except Exception as e:
    print('Hiba történt: ' +str(e)+ ' ugrás a következő blokkra!')



import re
from abc import ABC, abstractmethod


class Kerdes(ABC):
    def __init__(self, kerdes, helyesvalasz):
        self.kerdes = kerdes
        self.helyesvalasz = helyesvalasz

    def kerdest_feltesz(self):
        valasz = input(self.kerdes + "")
        helyes_e, plusz_info = self._valaszt_kiertekel(valasz)
        if helyes_e:
            print("A válasz helyes!")

        else:
            print(f"A válasz helytelen, a helyes válasz {self.helyesvalasz} lett volna. {plusz_info}" )
        return helyes_e

    @abstractmethod
    def _valaszt_kiertekel(self, valasz) -> (bool, str):
        pass


class Szoveges(Kerdes):
    def __init__(self, kerdes, helyesvalasz, minta):
        super().__init__(kerdes, helyesvalasz)
        self.minta = minta

    def _valaszt_kiertekel(self, valasz):
        return bool(re.search(self.minta, valasz)), ''

class Szam(Kerdes):
    def _valaszt_kiertekel(self, valasz):
        valasz_szam = int(valasz)
        if valasz_szam == self.helyesvalasz:
            return True, ''
        else:
            return False, f'Eltérés: {valasz_szam - self.helyesvalasz}'

class Kerdesek:
    def __iter__(self):
        self.kerdesek_es_valaszok = [
        Szam("Hány fokon a legsűrűbb a víz?", 4), Szam("Mikor volt a kiegyezés?", 1867), Szoveges("Mi Ausztria fővárosa?", "Bécs", r"^(bécs|Bécs|wien|Wien|vienna|Vienna)$" ),
        Szoveges('Melyik rajzfilmben szerepelt Gombóc Artúr?', 'Pop Pom meséi', r'^[Pp]om[ -]?[Pp]om( [Mm]eséi)?$'),]
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.kerdesek_es_valaszok):
            kerdes = self.kerdesek_es_valaszok[self.i]
            self.i += 1
            return kerdes
        else:
            raise StopIteration

try:
    for kerdes in Kerdesek():
        kerdesek_szama += 1
        if kerdes.kerdest_feltesz():
            pontszam += 1
except Exception as e:
    print('Hiba történt: ' +str(e))



import random
import re
from enum import Enum, auto

max = 2023
year = random.randint(1, max)


kerdesek_szama += 1

valasz = input(f'Szökőév volt-e az alábbi év: {year}?')
if year % 4 != 0:
    x = False
elif year % 400 == 0:
    x = True
elif year % 100 == 0:
    x = False
else:
    x = True

if x and valasz == 'igen':
    print('Helyes válasz!')
    pontszam += 1
elif not x and valasz == 'nem':
    print('Helyes válasz!')
    pontszam += 1
elif not x and valasz == 'igen':
    print("Helytelen válasz!")
elif x and valasz == 'nem':
    print("Helytelen válasz!")


print(f"Eredmény: {100*pontszam/kerdesek_szama:.3g} %")

valasz = input("Kíváncsi vagy, milyen osztályzatot érdemelsz?")

if valasz == 'igen':
    ossz_szazalek = 100*pontszam/kerdesek_szama
    if ossz_szazalek >= 85:
        print("Ötös!")
    elif ossz_szazalek >= 75:
        print('Négyes')
    elif ossz_szazalek >= 60:
        print('Hármas')
    elif ossz_szazalek >= 50:
        print('Kettes')
    else:
        print('Egyes!')
else:
    pass

print('Köszönöm a játékot! Szia!')