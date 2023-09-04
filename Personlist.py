print("En enkel personlig liste som hjelper kunden om å ha oversikt etter produktene deres.")

personlig_liste = []

def legg_til_produkt(produkt):
    personlig_liste.append(produkt)
    print(f"'{produkt}' ble lagt til i din personlige liste.")

def vis_liste():
    if personlig_liste:
        print("\nDin personlige liste: ")
        for i, produkt in enumerate(personlig_liste, start=1):
            print(f"{i}. {produkt}")
    else:
        print(" Din personlige liste er tom. ")

while True:
    print("\nMeny for Personlig Liste:")
    print("1. Legg til produkt")
    print("2. Vis liste")
    print("3. Avslutt")

    valg = input("Skriv inn ditt valg (1/2/3): ")

    if valg == '1':
        produkt = input("Skriv inn produktet du ønsker å legge til: ")
        legg_til_produkt(produkt)
    elif valg == '2':
        vis_liste()
    elif valg == '3':
        print("Ha det bra!")
        break
    else:
        print("Ugyldig valg. Vennligst velg et gyldig alternativ (1/2/3).")