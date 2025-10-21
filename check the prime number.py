num = int(input("Enter a number: "))

if (num <= 1):
    print (num, "is a not a prime number")

# check the numbers between 2 to input number
for i in range(2, num):

    #if the condition is true then execute the next statements
    #otherwise after the loop termination loop moves to else statment
    if num % i == 0 :
        print (num, "is not a prime number")
        break
else:
    print (num, "is a prime number")
