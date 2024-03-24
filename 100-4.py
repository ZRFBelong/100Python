#!/usr/bin/python3
#def square(a):
#    for i in a:
#        i = lambda i : i**2

numbers = [1,2,3,6,99,8,5,7]
maxim= max(numbers)
print(maxim)
numbers.sort()
print(numbers)
for i in numbers:
    i = lambda i : i**2
sortednumber=[]
#numbers.sort(key=square)
print(numbers)
#print(help(list.sort))
        
