'''Mathematical quadruple operations  whit if, elif and else function and for prime and non prime numbers we use the
modula method '''
print("Hallo, das ist hier der Taschenrechner")
print("Bitte wähle eine der folgenden Operationen:")
print("Addieren(A), Subtrahieren(S), Multiplizieren(M), Dividieren(D)")
operation: str = input()

is_valid: bool = True # wenn ich hier die operation false schreiben, kommt hier True. Warum?
print(is_valid)
if operation == "A":
    print("Du hast Addieren gewählt")
    print("Bitte gib zwei Zahlen zum Addieren ein!")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 + zahl2)

elif operation == "S":
    print("Du hast Subtrahieren  gewählt")
    print("Bitte gib zwei Zahlen zum Subtrahieren ein!")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 - zahl2)

elif operation == "M":
    print("Du hast  Multiplizieren gewählt")
    print("Bitte gib zwei Zahlen zum Multiplizieren ein!")
    zahl1 = int(input())
    zahl2 = int(input())
    print(zahl1 * zahl2)
elif operation == "D":
    print("Du hast Dividieren gewählt")
    print("Bitte gib zwei Zahlen zum DividierenD ein!")
    zahl1 = float(input())
    zahl2 = float(input())
    print(zahl1 / zahl2)
else:
    print("Deine aufgabe ist falsch!!")
    is_valid = False
print(is_valid)
if is_valid:

    operation: float = float(input("Geben sie die  ergebnis:"))
    if operation < 10:
        print("Hast du nicht gewonen,weil die ergebnis weing als 10 ist.")
    else:
        print("Du hast gewonen, weil die ergebnis mehr als 10 ist.")
    #ich möchte hier  nur gerade oder ungerade zahlen zeigen, aber weiß ich niht.
    print("Bitte geben sie die ergebnis noch mal:")
    zahl_gerade = int(input())
    if 10 % 2 == 0:  # modulo
        print("gerade juhu")  # Even
    else:
        print("ungerade oh oh")  # Odd # wenn die zahl ist ungrade das funktoioniert nicht?
    print("die programm ist bende!!!")
else:
    print("Das Programm wird jetzt beendet. Tschau")

''' by def function we build calculator for mathematical quadruple operation and we use also Global . But in general 
that methode means  recursion '''

# wir machen heute ein Taschenrechner , aber das ist anfanger.
#zuerst machen wir addtion :
def addtion(a, b):
    Resualt = a + b
    return Resualt
Resualt = addtion(3, 7)
print(Resualt)
#in zweite schritt machen wir zusammen multaflaction .
def multaflaction(a, b):
    Resulat = a - b
    return Resulat
Resulat = multaflaction(4,3)
print(Resulat)
# In dreitte schritt machen wir zusammen deviesion:
def deviesion(a, b):
    Resulat = a / b
    return Resulat
Resulat = deviesion(9, 3)
print(Resulat)
# we builden new python function
# def add(x, y):
#    return x + y

input_number = 6
def add_two():
    """ this function is always addinhg 2 to the input number"""
    global input_number
    input_number = input_number + 2
    return input_number
print(input_number)
print(add_two())
print(input_number)
print(add_two())
print(input_number)






