# SECURITY FUNCTIONS AND MAIN PROGRAM CALL

# A function that asks for a username. 
def userNameAgain(n):
    username = input("\nEnter username again: ")
    n

    if username == 'UzziKyle':
        passCode(3)

    else:
        n = n - 1
        print("\nInvalid username")

        if n != 0:
            print("You have (",n,") tries left")
            userNameAgain(n)

        else:
            invalid()


# A function that asks for a passcode. 
def passCode(n):
    passcode = int(input("Enter your four-digit passcode: "))
    n

    # If passcode is correct, it'll import the main program.
    if passcode == 1234:
        print('\n---------------------------------------------------')
        import Main

    # Else, it stops the program.
    else:
        n = n - 1
        print("\nInvalid passcode")
 
        if n != 0:
            print("You have (",n,") tries left\n")
            passCode(n)

        else:
            invalid()

# Will be called if the input has reached its error limit
def invalid():
    print("\nWho the hell are YOU!?")
    print("This is a secret program that intended for the use of a person you are certainly not.")

# StartUp - the start of the program, first attempt of asking the username
username = input("\nEnter your username: ")
if username == 'UzziKyle':
    passCode(3)

else:
    print("\nInvalid username")
    print("You have (",2, ") tries left")
    userNameAgain(2)