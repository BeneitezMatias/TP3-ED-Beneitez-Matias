from doubleLinkedList import DoubleLinkedList

listadoble=DoubleLinkedList()
i=1
while i<=10:
    listadoble.append(i)
    i+=1

print("===="*23)
print("lista completa, size:",len(listadoble))
print(listadoble)
print("===="*23)
print("cambia el valor en la posicion 3 por el 15")
listadoble.__setitem__(3,15)
print("devuelve el elememto en la posicion 3:",listadoble.__getitem__(3))
print("===="*23)
print("borra el elemento en la posicion 6")
listadoble.__delitem__(6)
print(listadoble,"\n","size:",len(listadoble))
print("===="*23)

