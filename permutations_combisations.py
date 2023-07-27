from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
s, k=input().split(' ')

'''
j=1
while j<=int(k):
    
    
    for i in list(permutations(sorted(s),int(j))):
        
        print(''.join(i))
    print('--------')

    
    for i in list(combinations(sorted(s),int(j))):
        print(''.join(i))
    j+=1
    print('__________')
'''
for i in list(combinations_with_replacement(sorted(s),int(k))):
        
        print(''.join(i))
