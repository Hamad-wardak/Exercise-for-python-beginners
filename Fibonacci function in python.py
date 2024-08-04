# i want chosse  to do the second simplay way for fibonacci calculated
'''Fibonacci saqeunce :
saqeunce of number where a number is the sum of the 2 numbers that came before it:
The saqeunce 'first digits are 0 and 1.
index:    1, 2, 3, 4, 5, 6, 7, 8, 9 ....
fibonacci:0, 1, 1, 2, 3, 5, 8, 13, 21 ...

Note: The zero is someteims not montioned '''

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

print(fibonacci(int(input('gieben sie bitte ein zahl ein:'))))              #pro
for x in range(int(input('gieben sie bitte ein zahl ein:'))):                #pro
    print(fibonacci(x))







