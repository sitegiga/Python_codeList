#check the number of letters in a string

my_string = "Hello world"
count = 0
for letter in my_string:
    if (letter == "l"):
     count += 1

print (count)

#check a substring

result = "a" in my_string
print (result)

result = "o" in my_string
print (result)