#String Mehtode (New):
'''
s= 'hallo world'
print(s.isalnum()) #checkt if the characters of s alphanumeric(a-z,A-Z and 0-9):True or False
print(s.isalpha()) #-------(a-z and A-Z):True or False
print(s.isdigit()) #-------(0-9):True or False
print(s.islower()) #-------are lowercase (a-z):True or False
print(s.isupper()) #-------are uppercase (A-Z):True or False
'''



#______________________________________#
'''
s= 'qA2'


l=list(s)

print(any([i.isalnum for i in l]))
print(any([i.isalpha for i in l]))
print(any([i.isdigit for i in l]))
print(any([i.islower for i in l]))
print(any([i.isupper for i in l]))
'''
#_____________________________________#




# rjust, ljust or center.

'''
text = 'python'
left=text.ljust(20,'-')
right=text.rjust(20,'-')

center=text.center(20,'-')

print(left)
print(right)
print(center)

'''



#_________________________________#

































