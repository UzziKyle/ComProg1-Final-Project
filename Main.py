# FUNCTIONS OF THE PROGRAM

# First and Catalyst function of the program.
def program(bound):

    # Calls the function bound to PPC Proper
    if bound == 1:
        pboundto1()

    # Calls the function bound to Sta. Monica
    elif bound == 0:
        pboundto0()

    # Repeats the question and function if user inputs invalid number
    else:
        print("\nInvalid Input. I'll kindly ask you again.")
        bound = int(input("\nCab is bound to? Bayan(1) or Sta. Monica(0) - please type the number: "))
        program(bound)

# This function will be called if the cab is bound to Sta. Monica.
# Will ask for the pickup point.
def pboundto0():

    # Pickup points
    plandmarks_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    plandmarks = ['PPC Proper', 'Junction 1', 'Asia World', 'First Consolidated Bank', 'Asturias', 'Seminario de San Jose', 'PSU', 'WPU', 'Sta. Monica']

    # Prints choices
    print("\nWhere is your pickup point?")
    for i, j in zip(plandmarks_id, plandmarks):
        print(f'{i} - {j}')

    # Asks for the desired option
    p = int(input("Enter the number of your pickup point: "))

    # Proceeds to dropoff options
    if p >= 0 and p <= 8:
        print("\nOkay. Got it.\n")
        dboundto0(p)

    # Repeats this function
    else:
        print("\nInvalid Number. I'll kindly ask you again.")
        pboundto0()

# Will ask for the dropoff point if bound to Sta. Monica.
def dboundto0(p):

    # Dropoff points
    dlandmarks_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    dlandmarks = ['PPC Proper', 'Junction 1', 'Asia World', 'First Consolidated Bank', 'Asturias', 'Seminario de San Jose', 'PSU', 'WPU', 'Sta. Monica']

    # Prints choices
    print("Here are some of the landmarks that'll be madadaanan by the cab on its way to Sta. Monica.")
    for i, j in zip(dlandmarks_id, dlandmarks):
        print(f'{i} - {j}')

    # Asks for the desired option
    d = int(input("Enter the number of your dropoff point: "))
    p 

    # Will run if input is within the given range
    if d >= 0 and d <= 8:
        print("\nSo you've chosen",dlandmarks[d], "as your dropping point?")
        yn = int(input("Yes(1)/No(0): "))

        if yn == 1:
            callprice(p,d)

        # Repeats this function
        elif yn == 0:
            print("\nOkay. Let me know your dropping point again.")
            dboundto0(p)

        # If the user inputs an invalid number when the two options given is very clear!
        else: 
            topak(yn)

    # Will run if the given number is out of the given range
    else: 
        print("\nInvalid Number")
        dboundto0(p)

# This function will be called if the cab is bound to PPC Proper.
# Will ask for the pickup point.
def pboundto1():

    # Pickup points
    plandmarks_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    plandmarks = ['Sta. Monica', 'WPU', 'PSU', 'Seminario de San Jose', 'Asturias', 'First Consolidated Bank', 'Asia World', 'Junction 1', 'PPC Proper']

    # Prints choices
    print("\nWhere is your pickup point?")
    for i, j in zip(plandmarks_id, plandmarks):
        print(f'{i} - {j}')

    # Asks for the desired option
    p = int(input("Enter the number of your pickup point: "))

    # Proceeds to dropoff options
    if p >= 0 and p <= 8:
        print("\nOkay. Got it.\n")
        dboundto1(p)

    # Repeats this function
    else:
        print("\nInvalid Number. I'll kindly ask you again.")
        pboundto1()

# Will ask for the dropoff point if bound to PPC Proper.
def dboundto1(p):

    # Dropping points
    dlandmarks_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    dlandmarks = ['Sta. Monica', 'WPU', 'PSU', 'Seminario de San Jose', 'Asturias', 'First Consolidated Bank', 'Asia World', 'Junction 1', 'PPC Proper']

    # Prints choices
    print("Here are some of the landmarks that'll be madadaanan by the cab on its way to PPC Proper.")
    for i, j in zip(dlandmarks_id, dlandmarks):
        print(f'{i} - {j}')

    # Asks for the desired option
    d = int(input("Enter the number of your dropoff point: "))
    p 

    if d >= 0 and d <= 8:
        print("\nSo you've chosen",dlandmarks[d], "as your dropping point?")
        yn = int(input("Yes(1)/No(0): "))

        if yn == 1:
            callprice(p,d)


        elif yn == 0:
            print("\nOkay. Let me know your dropping point again.")
            dboundto1(p)

        else: 
            topak(yn)

    else: 
        print("\nInvalid Number")
        dboundto1(p)

# When the user enters an invalid input when the given options are very clear!
def topak(n):
            n = n
            print("\nHilo ka ba?")
            print("Ang linaw linaw na\n0 at 1 lang ang option\n",n," ang inenter mo.")
            print("Sana okay ka lang.")
            print("Naiintindihan kita.")
            print("Bye!\n")

# This function will import Fareprice.py
def callprice(p,d):
            p
            d
            import Fareprice

            # Asks if passenger is eligible for a discount.
            status = int(input("\nStudent, Senior Citizen, or PWD? Yes(1)/No(0): "))

            # Displays the regular fare price
            if status == 0:
                Fareprice.regfareprice(p,d)

            # Displays the discounted fare price
            elif status == 1:
                Fareprice.discfareprice(p,d)

            else:
                topak()




# START OF THE PROGRAM

# First input of the main program.
bound = int(input("\nHello! Cab is bound to? Bayan(1) or Sta. Monica(0) - please type the number: "))

# Calls the functions of the programs.
program(bound)
