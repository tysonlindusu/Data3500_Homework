"""

1. Write a Python program that simulates a simple ATM machine. The program should ask the user for their account balance and then offer them the following 
options in a loop:

Check Balance
Deposit Money
Withdraw Money
Quit
If the user selects "Check Balance," display their current balance. If they select "Deposit Money," ask how much they want to deposit and update the balance 
accordingly. If they select "Withdraw Money," ask how much they want to withdraw and update the balance if they have sufficient funds. If they select "Quit," 
exit the program. Make sure to use nested if statements for handling these options.

2. Write a Python program to generate a multiplication table for a given number. Ask the user to enter a number, and then use the range() function to generate a table of multiplication from 1 to 10 for that number. For example, if the user enters 5, the program should print:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
"""

# ATM System

print('What is your balance? (because I am a very insecure ATM)')

user_balance = float(input())

still_transacting = True

while still_transacting == True:
    print('What would you like to do? \n1. Make a deposit \n2. Make a withdrawal \n3. Check your balance \n4. Exit')
    user_action = input()
    match user_action:
        case "1":
            print('How much would you like to deposit?')
            deposit_amount = float(input())
            user_balance += deposit_amount
        case "2":
            print('How much would you like to withdraw?')
            withdrawal_amount = float(input())
            if withdrawal_amount > user_balance:
                print('Insufficient funds.')
            elif user_balance > withdrawal_amount:
                user_balance -= withdrawal_amount
        case "3":
            print(f'Your balance is: {user_balance:.2f}')
        case "4":
            still_transacting = False
    
    print('Thank you for your business!')

    #Multiplication table

    print("Let's generate a multiplication table. Please enter a number: ")
    num = input()
    try:
        int(num)
    except ValueError:
        print('Invalid input, not a number')

    print('multiplier\tvalue')
    for i in range(1,11):
        print(f'{i} \t\t {int(num) * i}')