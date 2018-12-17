# ###########################################################
#                Python 3 while loop
# ###########################################################

# print number from 1 to 10
# hints: 1, 2, 3, ------ 10
number = 1
while number <= 10:
  print(number)
  number = number + 1

# print odd number from 1 to 10
# hints: 1, 3, 5, 7, 9
number = 1
while number < 10:
  print(number)
  number = number + 2

# print sum of numbers from 1 to 10
# hints: 1 + 2 + 3 + 4 + 5 + ----- + 10
# output should be: 55
number = 1
sum = 0
while number <= 10:
  sum = number + sum
  number += 1
print(sum)

# print sum of ODD numbers from 1 to 10
# hints: 1 + 3 + 5 + ----- + 9
# output should be: 25
number = 1
sum = 0
while number < 10:
  sum = number + sum
  number += 2
print(sum)

# ###########################################################
#                Python 3 for loop
# ###########################################################

# you have a item list including 3/4 items
# print every single item individually
# hints: The item is : Bread
# hints: The item is : Egg
# hints: The item is : Vegetable
# hints: The item is : Fish
item_list = ["bread", "egg", "vegetable", "fish"]
for item in item_list:
  print("The item is: ", item.title())

# print every Odd number from 1 to 10
# hints: 1, 3, 5, 7, 9
# use range function
for numbers in range(1, 10, 2):
  print(numbers)

# print every Even number from 1 to 20
# hints: 2, 4, 6, 8 ------ 20
for numbers in range(2, 22, 2):
  print(numbers)

# print Odd number from 1 to 10 but avoid print 5
# hints: 1, 3, 7, 9
for numbers in range(1, 10, 2):
  if numbers == 5:
    continue
  print(numbers)

# print Even number from 1 to 20
# if number is equal to 16 stop the program
# hints: 2, 4, 6 ------ 14
for numbers in range(2, 20, 2):
  if numbers == 16:
    break
  print(numbers)

