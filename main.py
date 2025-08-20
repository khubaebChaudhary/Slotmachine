#this is a global constant
MAX_LINES = 3

#this fucntion takes a valid input amount that the user wants to bet
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")

    return amount

#this fuction takes a valid number of lines and return that when function is called
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? $")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
