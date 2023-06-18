##1.Print numbers from 0 to 10 using while
x = 0
while x <= 10:
    print(x)
    x+=1

print('__________________________________________')

#___________________________________________________#

#2.Print numbers from 0 to 1o using for

for x in range(0,11):
    print(x)

print('__________________________________________')

#___________________________________________________#

#3.Stop the loop if the number = 5

for x in range(0,11):
    if x == 5:
     break
    print(x)

print('__________________________________________')


#___________________________________________________#

#4.Skip the 5 iteration from print

for x in range(0,11):
    if x == 5:
     continue
    print(x)

print('__________________________________________')


#___________________________________________________#

#5.Print multiplication table from 1 to 5

for x in range (1,6):
    for y in range (1,11):
        print(f'{x} * {y} =',x*y)
    print('----------')


print('__________________________________________')


#___________________________________________________#

#6.How to get numbers from 10 to 20 using range

for x in range (10,21):
    print (x)
print('__________________________________________')


#___________________________________________________#

#7.How to get numbers from 10 to 100 with 3 at each step using range


for x in range (10,101,3):
    print (x)
print('__________________________________________')


#___________________________________________________#

#8.Get a list of even numbers from 1 to 100 using for

for x in range (2,101,2):
  
        print(x)

print('__________________________________________')


#___________________________________________________#

#9.Get a list of even numbers from 1 to 100 using while

x = 1
while x <= 100:
    if x % 2 ==0:
        print(x)
    x+=1



print('__________________________________________')


#___________________________________________________#

#10.Get a list of even numbers from 1 to 100 using range



for x in range (1,101):
    if x % 2 == 0:
        print (x)
    
  
        

print('__________________________________________')

















