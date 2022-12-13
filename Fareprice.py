def regfareprice(x,y):
    kilometer = y - x

    if kilometer >= 0 and kilometer <= 4:
        print("\nYour fare is 12.00 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 5:
        print("\nYour fare is 13.75 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 6:
        print("\nYour fare is 15.50 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 7:
        print("\nYour fare is 17.50 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 8: 
        print("\nYour fare is 19.25 pesos.")
        print("\nThank you for using this program!")

    else:
        print("\nI can't comprehend what's just happened.")
        print("Sumasakit ang ulo ko.")
        print("Rerun na lang the program again. Thank you!")
        
def discfareprice(x,y):
    kilometer = y - x
    
    if kilometer >= 0 and kilometer <= 4:
        print("\nYour fare is 9.50 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 5:
        print("\nYour fare is 11.00 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 6:
        print("\nYour fare is 12.50 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 7:
        print("\nYour fare is 14.00 pesos.")
        print("\nThank you for using this program!")

    elif kilometer == 8: 
        print("\nYour fare is 15.25 pesos.")
        print("\nThank you for using this program!")

    else:
        print("\nI can't process what's just happened.")
        print("Sumasakit ang ulo ko.")
        print("Rerun na lang the program again. Thank you!")