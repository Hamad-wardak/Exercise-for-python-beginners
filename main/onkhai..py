# I wonto builden a Fabonacci formula:
print('which number do you want to calculate in Fibonacci, Enter here:')

# We have a function in math called Fibonacci: we can use this function to calculate different numbers.
#the function as already defined under , hier 1.618034 is fibancci´s constant

def f(x):
    y = (pow(1.618034, x)-pow((1-1.618034), x))/2.2360679774997896964091736687313
    return y

y = f(int(input('plase enter a  nummber for fibonacci calculated :')))
print(round(y))
c = int(input('plase enter a number for  series fibonacci calculated:'))
for x in range(c):
    print(round(f(x)))

print('The first calculated is end it')