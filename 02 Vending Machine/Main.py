# 02 Vending Machine
import logging

logging.basicConfig(level=logging.ERROR)

try:
    # Read the number of remaining cup from cup_file as text
    # Convert number_remaining_cups into a number
    file_cups = open("02 Vending Machine\cups.txt", "r")
    number_remaining_cups = int(file_cups.read())
    # Close the file cup.txt
    file_cups.close()
except:
    # Create a variable called number_remaining_cups of type int with the initial value 10
    number_remaining_cups = 10
    logging.debug("Some debugging information")


# Tell the user 'Welcome to IDE Hot Beverage service!'
print('Welcome to IDE Hot Beverage service!')
#Tell the user "There are " number_remaining_cups " cups left."
print("There are ", number_remaining_cups, " cups left.")

# Tell the user 'Here is what we offer:'
print('Here is what we offer:')
# Tell the user '1) Coffee'
print('1) Coffee')
# Tell the user '2) Tea'
print('2) Tea')

# Create a variable called choice of type number with the initial value 0
choice = 0
# Ask the user 'Type in your choice: ' and store the answer in choice
# Convert choice to integer and store in choice
try:
    choice_beverage = int(input('Type in your choice: '))
except ValueError as error:
    print("[",error,"]")
    print("Invalid choice...")
    choice_beverage = 0
    print("A black coffee is automatically selected")
finally:
    print("Selected: ", choice_beverage)
    



# Ask the user "Sugar (0-5): " and store the answer in sugar
choice_sugar = int(input("Sugar (0-5): "))
# Ask the user "Milk (y/n): " and store the answer in sugar
choice_milk = str(input("Milk (y/n): "))
# Create a variable called message of type string with the initial value ""
message = ""

# If choice is equal to 1
#     Then tell the user "Here is your coffee."
# Else serve a tea by default
#     Otherwise tell the user "Here is your tea."
if (choice_beverage == 1 or choice_beverage == 0) and choice_sugar == 0 and choice_milk == "n":
    # Add to message "Here is your black coffee."
    message += "Here is your black coffee. "
    # Decrease number of cups
    number_remaining_cups -= 1
elif choice_beverage == 1:
    # Add to message "Here is your coffee"
    message += "Here is your coffee. "
    # Decrease number of cups
    number_remaining_cups -= 1
elif choice_beverage == 2:
    message += "Here is your tea. "
    # Decrease number of cups
    number_remaining_cups -= 1
else:
    message += "Sorry, I do not know this choice. "


# Add to message whether the user take their beverage with or without sugar 
# Add to message whether they take their beverage with or without milk

# Tell the user whether they take their beverage with or without sugar
if choice_sugar >= 3:
    message += "With sugar. "
    # Add to message a 'healthy' comment
    message += "[Bitch that is too many sugar for yo ass] "
elif choice_sugar > 0:
    message += "With sugar. "
else:
    message += "Without sugar. "

# Tell the user whether they take their beverage with or without milk
if choice_milk == "y" or "y":
    message += "With milk. "
elif choice_milk == "n" or "N":
    message += "Without milk. "
else:
    message += "ERROR... "

# If choice is coffee without sugar nor milk



# Tell the user message
print(message)
# Tell the user "Have a great day!"
print("Have a great day!")
# Tell the user "BTW, there are " number_remaining_cups " cups left!"
print("BTW, there are ", number_remaining_cups, " cups left!")

# Open the file cups.txt in 'write' mode and keep it in the 'cup_file' variable
file_cups = open("02 Vending Machine\cups.txt", "w")
# Write number_remaining_cups in cup_file
file_cups.write(str(number_remaining_cups))
# Close the file cup.txt
file_cups.close()