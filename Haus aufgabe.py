import re

numbers = list([1, 2, 3, 4, 5])
# print("List before:", numbers)


numbers_calc = list()
for num in numbers:  # value
    if num % 2 == 0:
        numbers_calc.append(num)
    else:
        numbers_calc.append(num + 1)

for i in range(len(numbers)):  # reference
    numbers[i] = numbers[i] + 1

# print("List after:", numbers)


my_list = list(['abc', 'xyz', 'aba', '1221'])

my_string = "hello world"
# x = re.split("l", my_string)

for word in my_list:
    print(word[0])
# print(x)
