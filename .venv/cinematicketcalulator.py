costChildren = 5.0
costAdult = 10.0
costSenior = 7.5


def calculateTicket(ticketid):
    if ticketid == '1':
        return costChildren
    elif ticketid == '2':
        return costAdult
    elif ticketid == '3':
        return costSenior


cart = []

while True:
    cart.append(
        input("Welche Karte möchte sie kaufen? 1 für Kind, 2 für Erwachsener oder 3 für Senior (Q für bezahlen): "))
    if cart[-1] == "Q":
        cart.remove("Q")
        break

print(f"Es befinden sich {cart.__len__()} Karten in Ihrem Einkaufskorb.")

toPay = 0

for ticket in cart:
    toPay += calculateTicket(ticket)

print(toPay)
