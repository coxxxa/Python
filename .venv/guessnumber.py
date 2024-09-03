from random import randint

number = randint(1, 100)

# inital
guess = 0

print("Zahlenspiel")

while guess != number:
    try:
        guess = int(input("Rate welche Zahl ich bin "))
        if guess < number:
            print("Die Zahl ist größer")
        elif guess > number:
            print("Zahl ist kleiner")
        else:
            print("Herzlichen Glückwunsch, du hast die richtige Zahl gefunden!!!")
    except ValueError:
        print("Keine gültige Eingabe!")
