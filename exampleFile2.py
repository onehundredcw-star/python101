
# variable = input("this is an input that will take a response ")
# print(variable)

# height = int(input("How tall are you in inches? "))
# if height >= 48:
#     print("You may ride")
# else:
#     print("Sorry kid, get lost")

# password = "bluepen"
# userLoginInput = input("Enter password: ")
# if userLoginInput == password:
#     print("Login successful!")
# else:
#     print("Incorrect password.")

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# if number % 2 != 0:
#     print("The number is odd.")
# else:
#     print("The number is even.")

# for number in  range(1, 153):
#     print(number)

# for number in range(10, 0, -1):
#     print(number)
# print("Blast off!")

# numberOfRootBeers = int(input("How many bottles of root beer are on the wall? "))
# for i in range(numberOfRootBeers, 1, -1):
#     print(f"{i} bottles of root beer on the wall, {i} bottles of root beer. Take one down and pass it around, {i-1} bottles of root beer on the wall.")

total = 0
for number in range(1, 428):
    total += number
print(f"The total sum of numbers from 1 to 427 is: {total}")

while userLoginInput != password;
    print("Wrong password, try again.")
    userLoginInput = input("Enter password: ")
print("Login successful!")

numberList = [1, 4, 5, 4235, 42, -1]
largestNumber = numberList[0]
print(largestNumber)
for number in numberList:
    if number > largestNumber:
        largestNumber = number
print(f"The largest number in the list is: {largestNumber}")

secretNumber = 7
guess = 0
while guess != secretNumber:
    guess = int(input("Guess the secret number: "))
print("You got it!")