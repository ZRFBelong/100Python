number = [1,2,3,4,5,6,7,8,9]
print(sum(number))
print("$$$$$$$")
s=0
for i in number:
    s+=i
print(s)
####################################
def square(x):
    return (lambda x : x**3)(x)
a=square(66)
print(a)
##test lambda and map()
val = map(lambda x :x+2,number)
print(number,list(val))
