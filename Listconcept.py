# List slicing

"""my_list = ['q', 'a', 'd', 'e', 'e', 'r']

print (my_list)
print (my_list[1:3])
print (my_list[:6])
print (my_list[-2:])
print (my_list[::-1]) """
from idlelib.debugger_r import restart_subprocess_debugger

#append method add single item in the list

"""my_list = [1,2,3,4,5]
my_list.append(6)
print (my_list) """

#extend method add other list's item in the list

"""my_list = [1,2,3,4,5]
new_list = [7,8,9,10]
my_list.extend(new_list)
print (my_list)  """

#Nested list

my_list = [1,2,3,[4,5,6]]
result = my_list[3][0]
print (result)

for item in my_list:
    print (item)





