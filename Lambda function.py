#lambda function is a nameless function

x= int(input("Enter a number: "))
square = lambda n: n * n
print(square(x))

#this is an other function of anonymous(lambda) function
sum  = lambda a, b, c: a + b + c
print(sum(1,2,3))