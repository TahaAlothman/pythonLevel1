##1.Check if 10 is bigger than 15 or not
##2.If 10 is not bigger than15 print 10 is smaller than 15
if 10 > 15:
    print ('10 > 15')
else:
    print ('10 is smaller than 15')

    
print('_____________________________________')

##3.In which cases we will use all
##in condition ex :
x,y,z =2,4,6
if all([x==2 ,y==4, z==6]):
    print(True)
print('_____________________________________')

##4.What is the differences between all , and
print('What is the differences between all , and')
print('all is better to use when you may be comparing a varying amount of boolean statements and using and is much better for a finite boolean statement, and when using all, try to use a generator function.')

print('_____________________________________')

##5.What is the differences between any , or
print('What is the differences between any , or')
print('The or operator returns the first truthy value. That is, if you’re comparing two values that aren’t explicitly True or False, for example—say an empty string and a string that had a value— it would return the actual string value')


print('_____________________________________')


##6.If we need all the conditions to be true we will use
print('If we need all the conditions to be true we will use all')

print('_____________________________________')

##7.What is the differences between if , elif

print('What is the differences between if , elif')

print("Multiple if's means your code would go and check all the if conditions, where as in case of elif, if one if condition satisfies it would not check other conditions")


print('_____________________________________')

##8.What is the differences between elif else


print('What is the differences between elif else')

print("The else clause of an if statement is executed when the condition of the if statement results into false.The elif clause of an if statement is executed when there are multiple conditions in the if statement.Use if-else statements when the alternatives are mutually exclusive.Use if-elif-else statements when the alternatives are not mutually exclusive.elif acts like a ladder to capture extra but totally different conditions than if.")



print('_____________________________________')

##9.Can we use more than one elif

print('Can we use more than one elif')
print('yes we can')



print('_____________________________________')

##10.Can we use more than one else
print('Can we use more than one else')
print('no we can not')


print('_____________________________________')

##11.write s simple ternary operator

print("write s simple ternary operator python")

x = 11
print('x accept division by 2') if x % 2 == 0 else print('x accept not division by 2')

print('_____________________________________')

##12.in elif , python will check all the conditions no matter what ?


print('in elif , python will check all the conditions no matter what ?')

print('not elif ,but in the case of if')

print('_____________________________________')

##13. in elif we use else for ... ?

print('in elif we use else for ... ?')
print("Python first checks if the condition x < y is met. It isn't, so it goes on to the second condition, which in Python, we write as elif, which is short for else if. If the first condition isn't met, check the second condition, and if it’s met, execute the expression. Else, do something else. The output is “x is equal to y.")
      

print('_____________________________________')

##14.if we have this list [2,4,6,8,10] :
#1. check to see if 4 in this list or not
#2. check to see if 4 and 6 in this list on not
#3. check to see if 3 or 6 in this list
#4. check to see if 2 , 4 and 5 in this list

List= [2,4,6,8,10]

if 4 in List:
    print('4 in the List')

if 4 and 6 in List:
    print('4 and 6 in the List')
if 3 or 6 in List:
    print('3 or 6 in the List')
if 2 and 4 and 5 in List:
    print('2 and 4 and 6 in the List')


