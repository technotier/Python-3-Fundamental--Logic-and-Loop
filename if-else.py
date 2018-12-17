# Example 01
name = input("Enter Your Name Here: ")
age = int(input("Enter Your Age Here: "))

if age < 18:
  print("Sorry", name, "You are under 18. You are not allowed here...")
else:
  print("Welcome Here", name)

# Example 02
day = "Friday"

if day == "Friday":
  print("Let's go for watching Movie")
elif day == "Sat Day":
  print("Today is Holiday")
elif day == "Monday":
  print("Very Special Meeting with the Director")
else:
  print("Normal Working Day")

# Example 03
word = input("Enter a Word Here: ")
reverse_word = word[::-1]

if word == reverse_word:
  print(word, "is Pelidrome")
else:
  print(word, "is not Pelidrome")

# Example 04
print('Please, input the number:')
number = int(input())
temp = number

while number > 0:
  count = temp
  while count > 0:
    print('*', end='')
    count -= 1
  print()
  number -= 1



