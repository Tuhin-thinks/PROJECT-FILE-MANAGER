import os
print('enter the number of files you want to make? ')
number=int(input())
print('Enter the type of file you want to create?')
typ=input()
c=0
for i in range(number):
    open(typ[1:]+str(i+1)+typ,mode='w')
    c+=1
print('{} files created successfully'.format(c))