#PROGRAM TO CONVERT FROM SOLES TO DOLLARS, AND VICEVERSA
# 
# 
# 
# INPUT
option = 0
while(option != 3):
    print("""
    ==================================================================
            MONEY CONVERTER - VERSION 1.0
    ==================================================================
    OPTION 1 : CONVERT FROM SOLES TO DOLLARS
    OPTION 2 : CONVERT FROM DOLLARS TO SOLES
    OPTION 3 : EXIT
    ==================================================================
    """)
    option = int(input("Enter an option of the menu: "))

    # PROCESS
    if(option == 1):
        #CONVERT FROM SOLES TO DOLLARS
        originAmount = input("Enter the amount in soles : ")
        destinyAmount = float(originAmount) / 3.8
        destinyCurrency = "dollars"

    elif(option == 2):
        #CONVERT FROM DOLLARS TO SOLES
        originAmount = float(input("Enter the amount in dollars : "))
        destinyAmount = originAmount * 3.9
        destinyCurrency = "soles"

    elif(option == 3):
        print("So long !!!")

    else:
        print("You must enter an abovementioned valid option")

# OUTPUT 
    if(option <= 2 and option >=1 ):
        print("The amount in " + destinyCurrency + " is " + str(destinyAmount))