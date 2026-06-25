print("Hello, World!")
print("My name is Chris")

# ctrl+/ is how we make a comment
learner = "Chris"
print(learner)

ideal_number_of_pets = 2
print(ideal_number_of_pets)

# this is a float variable
how_much_is_a_banana = 9.99
print(how_much_is_a_banana)

# this is a boolean variable
are_our_pets_vaccinated = True
print(are_our_pets_vaccinated)

# print(type(learner))
# print(type(ideal_number_of_pets))
# print(type(how_much_is_a_banana))
# print(type(are_our_pets_vaccinated))

# is_it_a_number = 333
# is_this_a_number = "333"

# print(type(is_it_a_number))
# print(type(is_this_a_number))

# print(5+3)
# print(5*3)
# print(5/3)

# example of modulo
print(10%3)
print(10/3)

# example of exponential
print(2**5)
print(2**2)
print(32**73)

# find the area of a rectangle
# length = input("What is the length of the rectangle? ")
# length = int(input("What is the length of the rectangle? "))
# # width = 20
# width = int(input("What is the width of the rectangle? "))

# area = length * width

# print(area)

# # find the tax amount
price = 10
tax = price * 0.08

print(f"The tax amount is {tax}")

# # find the average
avg = (10+10+10)/3

print(f"The average is {avg}")

# ask the user their favorite color
fav_color = input("what is your favorite color? ")

# print(fav_color)
print(f"Your favorite color is {fav_color}")

# test multiple inputs
print("This","is","what","they","are","talking","about")

print(12, 24, -2, sep=':')
print('but','not','including', sep='**')

# create a receipt
# customer name
# the price of what they purchased
# the quantity of the product they purchased
# the total cost
customerName = input("Enter customer's name:")
itemPrice = int(input("what is the cost of the item? "))
quantity = int(input("how many of the item did they purchase? "))
totalCost = itemPrice * quantity
roundedCost = round(totalCost, 2)
print("Receipt")
print(f"Customer Name: {customerName}")
print(f"Item price: ${itemPrice}")
print(f"quantity: {quantity}")
print(f"Total cost: ${totalCost}")
print(f"Rounded cost: ${roundedCost}")