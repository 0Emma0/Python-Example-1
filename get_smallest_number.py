# Purpose: This program asks the user to input a list of numbers and then calculates the smallest number in the list.
# Usage: python get_smallest_number.py

# Function to compare two numbers and get the smaller one
def get_smaller_number(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Initialize the variable to store the smallest number
smallest_number = None

# Print instructions for the user
print("Enter a list of numbers. Press Enter after each number.")
print("When you want to calculate the smallest number, enter 'X' and press Enter.")

# Create a loop for the user to input numbers
while True:
    # Ask the user to input a number or 'X' to end
    user_input = input("Enter a number (or 'X' to get the smallest number): ")
    
    # Check if the user wants to end the process
    if user_input.upper() == 'X':
        # If the user inputs 'X', show the smallest number and end the program
        print("The smallest number entered is:", smallest_number)
        break
    else:
        try:
            # Try to convert the user's input to an integer
            number = int(user_input)
            # Check if it's the first time a number is entered
            if smallest_number is None:
                # If it's the first time, assign the entered number as the smallest
                smallest_number = number
            else:
                # If it's not the first time, compare the entered number with the current smallest number
                smallest_number = get_smaller_number(smallest_number, number)
        except ValueError:
            # If the input is not a valid number, show an error message
            print("Please enter a valid number.")

