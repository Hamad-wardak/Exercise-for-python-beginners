''' in this formula use we for prime and non-prime numbers calculated (modula) method . if the result is True
 then it is not a prime number and if the result is Fals'''

from math import sqrt
n = int(input('which numbers do you want to calculate? please enter this number: '))
# this flag maintains status whether the n is prime or not
prime_flag = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")

'''the second way for prime and non o´´prime number calculated'''
# Variable definition and assignment
inputn= int(input("Bitte geben sie ein zahl ein :"))

# Taking user input
# inputn = int(input("Enter a number: "))

if inputn > 1:  # input ist größer als 1
    # check for factors
    for i in range(2, inputn):  # i von 2 bis input
        if (inputn % i) == 0:
            print(inputn, "ist nicht ein primzahl.")
            print(i, "times", inputn // i, "is", inputn)
            break
    else:
        print(inputn, "ist ein primzahl.")

# If the input number is less than or equal to 1, then it is not prime
else:
    print(inputn, "is not a prime number.")


    #diese unter ist ein neu untericht.


a = 0


def funktion(i):
    if i == 3:
        return i  # Ende
    a = i + 1
    return funktion(a)


print(funktion(a))
