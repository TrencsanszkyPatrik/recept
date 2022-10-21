hozzavalok = """15 dkg mix salátalevél
 2 db őszibarack
 1 fej lilahagyma
 5 dkg dió
 6 dkg feta
 4 ek olívaolaj
 2 ek citromlé
 1 tk méz
 ½ tk só
 ¼ tk őrölt bors\n"""

elkeszites = """1, A salátaleveleket megmossuk és félre tesszük. Az őszibarackot megmossuk és felszeleteljük, a diót durvára vágjuk. A hagymát apróra vágjuk. A fetát felkockázzuk.
 2, Az olívaolajat, a citromlevet, a mézet, a sót és a borsot összekeverjük, a felét a salátalevelekre öntjük.
 3, Ezután hozzáadjuk a barackot, a hagymát, a diót és a fetát, végül a maradék öntettel meglocsoljuk a salátát.\n"""

def menu():
    print("Válassz receptet!\nElérhető receptek: 'Saláta'")
    print("A kilépéshez pedig írd be hogy 'Kilépés', 'kilépés', vagy pedig 'Exit''")
    valasz = input("Írd be a recept nevét: ")

    if valasz == "Saláta" or "saláta":
        salata()
    elif valasz == "kilépés" or "Kilépés" or "Exit":
        exit()
    else:
        print("Nincs ilyen választási lehetőség, próbáld újra! ")
        menu()


def salata():
    dontes = input("Válassz az opciók közül: \n 1, Hozzávalók. \n 2, Elkészítés \n 3, Vissza a menübe\n 4, Kilépés\n" )

    match dontes:
        case "1":
            print("Jelenleg ebbe a menüpontba vagy: Hozzávalók \n", hozzavalok)
            vissza = input("Vissza szeretnél menni az előző menüponthoz? ")
            if vissza == "Igen" or "igen":
                salata()
            else: menu()
        case "2":
            print("Jelenleg ebbe a menüpontba vagy: Elkészités \n", elkeszites)
            vissza = input("Vissza szeretnél menni az előző menüponthoz? ")
            if vissza == "Igen" or "igen":
                salata()
            else: menu()
        case "3":
            menu()
        case "4":
            exit()
        case _:
            print("Helytelen választási lehetőség, próbáld újra\n")
            salata()


menu()