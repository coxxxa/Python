shoppinglist = []


# Artikel hinzufügen
# Aktion -> hinzufügen, entfernen, anzeigen und beenden

def printMenu():
    print("1. Hinzufügen")
    print("2. Entfernen")
    print("3. Anzeigen")
    print("4. Beenden")


def showShoppingList():
    print(shoppinglist)


def insertToShoppingList(item):
    if item in shoppinglist:
        print(f"{item} bereits auf der Einkaufsliste")
    else:
        shoppinglist.append(item)


def removeFromShoppingList(item):
    try:
        shoppinglist.remove(item)
        print(f"{item} wurde aus der Einkaufsliste entfernt!")
    except ValueError:
        print(f"{item}, steht nich auf der Einkaufsliste!")
    finally:
        showShoppingList()

def copyShoppingList(shoppinglist):
    print("Einkaufsliste wurde kopiert...")


def switchMenu(id):
    if id == 1:
        print("Hinzufügen")
        continueAdd = True
        while continueAdd:
            newItem = input("Was willst du auf die Einkaufsliste setzen (q zum beenden): ")
            if newItem == "q": break
            insertToShoppingList(newItem)
        return 1
    elif id == 2:
        print("Entfernen")
        showShoppingList()
        continueAdd = True
        while continueAdd:
            removeItem = input("Was willst du aus der Einkaufsliste enfernen (q zum beenden): ")
            if removeItem == "q": break
            removeFromShoppingList(removeItem)
        return 1
    elif id == 3:
        print("Anzeigen")
        showShoppingList()
        return 1
    elif id == 4:
        print("Wir sind fertig!")
        return -1
    else:
        print(f"{id}, ist keine gültige Auswahl!")


controlVar = 1

while controlVar == 1:
    printMenu()
    controlVar = switchMenu(int(input("Was möchten Sie tun, Menüpunkt wählen: ")))
