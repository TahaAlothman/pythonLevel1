##Task Variables
#1.create a Boolean Variable named x
x=True
print ("x is ",type (x))
print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#2.Create an integer variable named y
y = 5
print ("y is ",type (y))
print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#3.Create a float variable named z
z = 1.4

print("z is ",type (z))
print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#4.Create a string variable names s
s='Taha'
print ("s is ",type (s))
print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#5.Convert the int variable to float
a = 4

print('a is',type (a))

a=float (a)
print('a class has been changed to ', type(a))

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#6.Can we convert the str to int ?
num = '5'

print('num is ',type(num))


num = int(num)


print('num class has been changed to ',type(num))

# We can check by doing some mathematical operations
print(num + 20)

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#7.Create a list of numbers from 1 to 5

list_of_numbers = list(range(1, 6))

print(list_of_numbers)

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#8.Create a tuple from 10 to 15


my_tuple = tuple(range(10,16,1))

print (my_tuple)

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#9.Convert the list to tuple
num_list = [1,2,3]

print (num_list,type(num_list))

num_list = tuple ([1,2,3])

print ((num_list),type(num_list))

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#10.Create a dict of 3 values

my_information = {'name': 'Taha', 'age': 32, 'location': 'Germany'}

print(my_information)

print(type(my_information))

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#11. Can we use semi colon ; with python

x1 = 32; x2 = "Taha"; print(f"my Name ist {x2} and i am {x1} years old ");
print("yes,we can use Semi colon with python,but Python does not require semicolons to terminate statements");

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#12.Python is interpreted or compiled ?

print("Python is interpreted or compiled?")
print("python is both,interpreted and compiled")

print ('_____________________________________')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#13. What is the differences between low level &high level
print('What is the differences between low level &high level')

print ("**Low Level:")
print(" Do not feature abstraction ,Are readable by machines, and are not close to human language Involve memory management Examples include assembly language and machine code")
print ("**High Level:")
print(" Feature abstraction ,Are closer to human languages, and are more readable Do not deal with memory management Examples include: Java, Python, Ruby, and C#")






