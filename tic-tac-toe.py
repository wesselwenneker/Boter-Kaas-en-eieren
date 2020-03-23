import random
gewonnen = "false"
stop = ''
stoppen = "nee"
bord = ["", "___", "___", "___",
        "___", "___", "___",
        "___", "___", "___",]

bord1 = ["","_1_","_2_","_3_",
        "_4_","_5_","_6_",
        "_7_","_8_","_9_"]

def laat_bord_zien1():
    print(" ___ ___ ___")
    print("|_1_|_2_|_3_|")
    print("|_4_|_5_|_6_|")
    print("|_7_|_8_|_9_|")

def laat_bord_zien():
    print(" ___ ___ ___")
    print("|" + bord[1] + "|" + bord[2] + "|" + bord[3] + "|")
    print("|" + bord[4] + "|" + bord[5] + "|" + bord[6] + "|")
    print("|" + bord[7] + "|" + bord[8] + "|" + bord[9] + "|")

def een_beurt(beurt, lijst_1, lijst_2):
    if beurt == "X":
        invoer_1 = int(input(""))
        while str(invoer_1) in lijst_1 or str(invoer_1) in lijst_2 or invoer_1 > 9:
            laat_bord_zien1()
            laat_bord_zien()
            print("Dat kan niet")
            invoer_1 = int(input(""))
        lijst_1 += str(invoer_1)
        lijst_1.sort()
        bord[invoer_1] = "_X_"
        laat_bord_zien1()
        laat_bord_zien()
    elif beurt == "O":
        invoer_2 = int(input(""))
        while str(invoer_2) in lijst_1 or str(invoer_2) in lijst_2:
            laat_bord_zien1()
            laat_bord_zien()
            print("Dat kan niet")
            invoer_2 = int(input(""))
        lijst_2 += str(invoer_2)
        lijst_2.sort()
        bord[invoer_2] = "_O_"
        laat_bord_zien1()
        laat_bord_zien()
    elif beurt == 'De computer':
        getallen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        keuze = random.choice(getallen)
        while str(keuze) in lijst_1 or keuze in lijst_2:
            keuze = random.choice(getallen)
        lijst_2 += str(keuze)
        lijst_2.sort()
        print(keuze)
        bord[int(keuze)] = "_O_"
        laat_bord_zien1()
        laat_bord_zien()

def Kijken_of_gewonnen(beurt, index):
    row1 = bord[1] == bord[2] == bord[3] != "___"
    row2 = bord[4] == bord[5] == bord[6] != "___"
    row3 = bord[7] == bord[8] == bord[9] != "___"
    collumn1 = bord[1] == bord[4] == bord[7] != "___"
    collumn2 = bord[2] == bord[5] == bord[8] != "___"
    collumn3 = bord[3] == bord[6] == bord[9] != "___"
    diagonal1 = bord[1] == bord[5] == bord[9] != "___"
    diagonal2 = bord[3] == bord[5] == bord[7] != "___"
    if index >= 9:
        return "Gelijkspel"
    if row1 or row2 or row3 or collumn1 or collumn3 or collumn3 or diagonal1 or diagonal2:
        return beurt
    else:
        return False


def main(spelers):
    if spelers == "2":
        index = 0
        lijst_1 = []
        lijst_2 = []
        laat_bord_zien1()
        laat_bord_zien()
        beurt = "X"
        Kijken_of_gewonnen(beurt, index)
        while True:
            beurt = "X"
            een_beurt(beurt, lijst_1, lijst_2)
            index += 1
            Kijken_of_gewonnen(beurt, index)
            if Kijken_of_gewonnen(beurt, index) == beurt:
                print(beurt + " wint")
                break
            elif Kijken_of_gewonnen(beurt,index) == "Gelijkspel":
                print("Gelijkspel")
                break
            beurt = "O"
            een_beurt(beurt, lijst_1, lijst_2)
            index += 1
            Kijken_of_gewonnen(beurt, index)
            if Kijken_of_gewonnen(beurt,index) != False:
                print(beurt + " wint")
                break
    elif spelers == "1":
        index = 0
        lijst_1 = []
        lijst_2 = []
        laat_bord_zien1()
        laat_bord_zien()
        beurt = "X"
        Kijken_of_gewonnen(beurt, index)
        while True:
            beurt = "X"
            een_beurt(beurt, lijst_1, lijst_2)
            index += 1
            Kijken_of_gewonnen(beurt, index)
            if Kijken_of_gewonnen(beurt, index) == beurt:
                print(beurt + " wint")
                break
            elif Kijken_of_gewonnen(beurt,index) == "Gelijkspel":
                print("Gelijkspel")
                break
            beurt = "De computer"
            een_beurt(beurt, lijst_1, lijst_2)
            index += 1
            Kijken_of_gewonnen(beurt, index)
            if Kijken_of_gewonnen(beurt,index) != False:
                print("De computer wint")
                break

while stoppen != "ja":
    spelers = input("Met hoe veel spelers wil je spelen?(1/2) ")
    main(spelers)
    stoppen = input("wil je stoppen?(ja/nee) ")