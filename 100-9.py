import re
string1 = "my name is zhang ,age is 18"
string3 = re.sub(r'\d','#',string1)
print(string3)
string2 = string1.replace('zhang','wang')
print(string2)
with open('poem.txt','r',encoding='utf-8') as f :
    context = f.read()
print(type(context))
print(context)
