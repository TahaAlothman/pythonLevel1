#1.Create a simple function that takes 2 numbers and print their values

def mysum(x,y):
    print('x =' ,x,' ,y =',y)


mysum(5,1)


    
print ('_____________________________________')

#______________________________________________________#


#2.Create a simple function that takes 2 numbers and return their values

def mysum2(x,y):
    return x ,y

a = mysum2(3,4)
print(a)


print ('_____________________________________')

#______________________________________________________#


#3.In the above return function , use keywordarguments when calling the function

def mysum2(x,y):
    return x ,y

a = mysum2(y=3,x=4)
print(a)


print ('_____________________________________')

#______________________________________________________#


#4.In the above return function , give x and y default values of 0 and call the function with no arguments



def mysum2(x=0,y=0):
    return x ,y

a = mysum2()
print(a)


print ('_____________________________________')

#______________________________________________________#


#5.Create a function that can take any number of arguments and print the sum of them


def mysum2(x,y):
    return x + y

a = mysum2(4,6)
print(a)


print ('_____________________________________')


#______________________________________________________#


#6.Create the same sum function using the lambda


mysum = lambda x,y,z: (x+y+z)

print (mysum(1,2,4))

print ('_____________________________________')




#______________________________________________________#


#7.Call the lambda function at the same definition line

mysum = lambda x,y,z: (x+y+z); print (mysum(1,2,4))


print ('_____________________________________')




#______________________________________________________#


#8.Write the difference between the local variable and global variable Python Functions Tasks
 print (' Global variables are declared outside the functions whereas local variables are declared within the functions')








