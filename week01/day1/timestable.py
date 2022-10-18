#INPUT

table = input("Enter times table : ")




#PROCESS
for counter in range(1,13,1):
    #OUTPUT
    print(table + " x " + str(counter) + " = " + str(counter * int(table)))



