import sys

gracz1 = 0
gracz2 = 0

while gracz1 < 3 and gracz2 < 3:
    wybor_gracz1 = input("Gracz 1 podaj swój wybór: ")
    wybor_gracz2 = input("Gracz 2 podaj swój wybór: ")

    if wybor_gracz1 == "papier":
        if wybor_gracz2 == "kamien" or wybor_gracz2 == "kamień":
            print("Gracz 1 wygrał!")
            gracz1 += 1
        elif wybor_gracz2 == "papier":
            print("Remis!")
            gracz1 and gracz2 + 1
        else:
            print("Gracz 2 wygrał!")
            gracz2 += 1

    # gracz 1 nożyczki
    elif wybor_gracz1 == "nozyczki" or wybor_gracz1 == "nożyczki":
        if wybor_gracz2 == "papier":
            print("Gracz 1 wygrał!")
            gracz1 += 1
        elif wybor_gracz2 == "nozyczki" or wybor_gracz2 == "nożyczki":
            print("Remis!")
            gracz1 and gracz2 + 1
        else:
            print("Gracz 2 wygrał!")
            gracz2 += 1

    # gracz 1 kamień
    elif wybor_gracz1 == "kamien" or wybor_gracz1 == "kamień":
        if wybor_gracz2 == "nozyczki" or wybor_gracz2 == "nożyczki":
            print("Gracz 1 wygrał!")
            gracz1 += 1
        elif wybor_gracz2 == "kamien" or wybor_gracz2 == "kamień":
            print("Remis!")
            gracz1 and gracz2 + 1
        else:
            print("Gracz 2 wygrał!")
            gracz2 += 1

    # jeśli gracz poda coś innego
    else:
        print("Wybierz papier, kamień lub nożyczki!")

if gracz1 == 3:
        print(f"Gracz 1: {gracz1}, Gracz 2: {gracz2} \n")
        print("Koniec gry, wygrał Gracz 1!\n")
        sys.exit()

if gracz2 == 3:
        print(f"Gracz 1: {gracz1}, Gracz 2: {gracz2} \n")
        print("Koniec gry, wygrał Gracz 2!\n")
        sys.exit()

if gracz1 == gracz2:
        print(f"Gracz 1: {gracz1}, Gracz 2: {gracz2} \n")
        print("Nikt nie wygrał, remis!\n")
        sys.exit()
