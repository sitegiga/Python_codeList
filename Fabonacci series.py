a = 0
b = 1

num = int(input("enter a number to find fabonacci series: "))
print(a)
print(b)

# range between 2 to input number because 1st two numbers already printed
for i in range(2,num):

    c = a + b
    a = b
    b = c
    print(c)
