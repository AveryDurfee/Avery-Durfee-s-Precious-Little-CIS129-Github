#Avery Durfee 3/13/2024

def main():
    while True:
        user_number = get_integer("Input a number: ")
        if is_it_even(user_number):
            print("Number is even.")
        else:
            print("Number is odd.")
        again = input("enter \'y\' to loop again")
        if again != "y":
            break
#Input with validation
def get_integer(message):
    while True:
        try:
            user_input = int(input(message))
            break
        except ValueError:
            print("Input is not a valid number.")
    return user_input
#Checks if number is even.
def is_it_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()