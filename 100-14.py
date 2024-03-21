lista = [0,1,1,1,2,2,2,2,2,2,3,4,5,6]
dicta = {}

for i in lista:
    if i not in dicta:
        dicta[i] = 1
    else:
        dicta[i] += 1
#dicta.sort()
print(dicta)


