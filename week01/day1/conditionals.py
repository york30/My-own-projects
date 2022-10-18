#INPUT


number1 = input("Number 1: ")
number2 = input("Number 2: ")

operation = input("Operation to execute(Addition, Sustraction) : ")

#Process


if(operation == "addition"):
    result = int(number1) + int(number2)

elif(operation == "sustraction"):
    result = int(number1) - int(number2)

else:
    result = ""




#OUTPUT

if (result == ""):
    print("You must enter a valid operation")
else:
    print("The result is : " + str(result))

print("So long!")
