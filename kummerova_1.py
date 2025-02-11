"""
kummerova_1.py: první projekt do Engeto Online Python Akademie

author: Pavlína Kummerova 
email: paja.kummerova@seznam.cz
"""

#zadane texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# registrovani uzivatele
uzivatele = [
    {"bob": "123"},
    {"ann": "pass123"},
    {"mike": "password123"},
    {"liz": "pass123"}
    ]

#Prihlaseni 
#definice prihlasovacich udaju vstupem od uzivatele
prihlasovaci_udaje = {
    f"{input("login: ")}": f"{input("password: ")}"
    }

#kontrola udaju

if prihlasovaci_udaje not in uzivatele:
    print("unregistered user, terminating the program..")
    quit()
    


#ulozeni loginu do promenne
# - pouzita funkce keys(), ktera vraci objekt preveditelny na list
login = list(prihlasovaci_udaje.keys())[0]

#vypsani uvodu
print(
    "----------------------------------------\n"+
    f"Welcome to the app, {login}\n"+
    "We have 3 texts to be analyzed.\n"+
    "----------------------------------------"
    )

#Cyklus zvoleni textu
# - zastavi se pouze pri validnim zvoleni
while True:
    #vstup uzivatele a validni moznosti
    volba = input("Enter a number btw. 1 and 3 to select: ")
    validni_volby = ["1", "2", "3"]
    print("----------------------------------------")

    #samotny cyklus
    if volba in validni_volby: 
        zvoleny_text = TEXTS[int(volba) - 1]
        break
    else:
        continue

#Analyza textu
#=============
#rozdeleni textu do seznamu slov a zjisteni poctu
slova = str(zvoleny_text).replace(".", "").split()

#deklarace promennych pro pocty
slova_title = []
slova_upper = []
slova_lower = []
slova_numeric = []
slova_sum = 0
nejdelsi_delka = 0
cetnosti = {}
serazene_cetnosti = {}

#vytazeni slov do ruznych skupin
for slovo in slova:
    #titlecase
    if slovo.istitle():
        slova_title.append(slovo)
    #uppercase
    elif slovo.isupper():
        slova_upper.append(slovo)
    #lowercase
    elif slovo.islower():
        slova_lower.append(slovo)
    #numeric
    elif slovo.isnumeric():
        slova_numeric.append(slovo)

    #identifikace nejdelsi delky
    if len(slovo) >= nejdelsi_delka:
        nejdelsi_delka = len(slovo)

#count vsech seznamu
pocet_title = len(slova_title)
pocet_upper = len(slova_upper)
pocet_lower = len(slova_lower)
pocet_numeric = len(slova_numeric)

#sum numerickych slov
for temp in slova_numeric:
    slova_sum = int(slova_sum) + int(temp)


print(
    f"There are {len(slova)} words in the selected text\n" +
    f"There are {pocet_title} titlecase words.\n" +
    f"There are {pocet_upper} uppercase words.\n" +
    f"There are {pocet_lower} lowercase words.\n" +
    f"There are {pocet_numeric} numeric strings.\n" +
    f"The sum of all the numbers {slova_sum}\n" +
    "----------------------------------------"
) 

#vypocet cetnosti

for slovo in slova:
    if f"{len(slovo)}" in cetnosti.keys():
        cetnosti[f"{len(slovo)}"] += 1
    else:
        cetnosti.update({f"{len(slovo)}": 1})

#sort klicu prevedenych na seznam
serazene_klice = sorted(list(cetnosti.keys()), key = int)

#sort cetnosti
for klic in serazene_klice:
    serazene_cetnosti.update({klic: cetnosti.get(klic)})

#Vytvoreni grafu
#===============
# - potrebne promenne
hodnoty = list(serazene_cetnosti.values())
hodnoty_hvezdy = []
cislo_radku = 1

# - zjisteni poctu mezer pro titul grafu (definice sirky grafu)
nejvetsi_cetnost = max(hodnoty)
if nejvetsi_cetnost <= 12:
    mezery_titul = "  "
else:
    mezery_list = []
    pocet_mezer = 0
    pocet_mezer_titul = ((nejvetsi_cetnost - len("OCCURENCES")) / 2) + 1
    while pocet_mezer < pocet_mezer_titul:
        mezery_list.append(" ")
        pocet_mezer += 1
    mezery_titul = "".join(mezery_list)


# - nadepsani sloupcu grafu
nadpis = f"LEN|{mezery_titul}OCCURENCES{mezery_titul}|NR."
print(nadpis)
print("----------------------------------------")

# - vytvoreni seznamu stringu hvezd
for x in hodnoty:
    pocitadlo = 0
    hvezdy = []
    while pocitadlo < x:
        hvezdy.append("*")
        pocitadlo += 1
    hodnoty_hvezdy.append("".join(hvezdy))

# - vypsani grafu do konzole
for radek in hodnoty_hvezdy:
    pocet_mezer = 10 + len(mezery_titul)*2 - len(radek)
    string_mezer = []
    pocitadlo_2 = 0

    while pocitadlo_2 < pocet_mezer:
        string_mezer.append(" ")
        pocitadlo_2 += 1
        
    # - sestaveni radku
    print(f"%3d|{radek}{"".join(string_mezer)}|{len(radek)}" % (cislo_radku, ))
    cislo_radku += 1