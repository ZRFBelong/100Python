lista = [1,3,5,7,9]
listb = [2,4,6,8,0]
listc = lista.extend(listb)
print(listc)
print("#####")
print(lista)
listd = [99]
for i in lista :
    listd.append(i)
print(listd)

liste = lista + listb
print(liste)
print(type(liste))
