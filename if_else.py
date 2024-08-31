print("Hallo, das hier ist der Taschenrechner")
print("Bitte wähle eine der folgenden Operationen:")
print("Addieren(A), Subtrahieren(S), Multiplizieren(M), Dividieren(D)")
operation: str = input()

if operation == "A":
    print("Du hast Addieren gewählt")
    print("Bitte gib zwei Zahlen zum Addieren ein!")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 + zahl2)

elif operation == "S":
    print("Du hast Subtrahieren gewählt")
    print("Bitte gib zwei Zahlen zum Subtrahieren ein!")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 - zahl2)
elif operation == "M":
    print("Du hast multiplizieren gewahlt")
    print("Bitte geben sie zwei zahlen zum multiplizieren ein")
    zahl1 = input()
    zahl2 = input()
    print(int(zahl1) * int(zahl2))
elif operation == "D":
    print("Du hast Divideren gewahlt  ")
    print("Geben sie zwei zahl ein:")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 / zahl2)
else:
    print("Deine Eingabe war falsch. Bitte starte das Programm neu! <3")
