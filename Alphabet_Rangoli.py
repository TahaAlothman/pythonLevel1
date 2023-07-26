'''
input: integer number
output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
def print_rangoli(size):
   alpha=[chr(i) for i in range(97,123)]
   alpha=alpha[:size]
   index=list(range(size))
   index=index[:-1] + index[::-1]
   for i in index:
        start= i + 1
        original=alpha[-start:]
        reverse=original[::-1]
        row=reverse + original[1:]
        row= "-".join(row)
        width=size*4 -3
        row=row.center(width,"-")
        print (row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
