from linkedStackExt import LinkedStackExt

pila=LinkedStackExt()
#añade datos a la pila
i=0
while i<10:
    pila.push(i)
    i+=1

print("===="*23)
print("pila completa")
print(pila)

print("===="*23)
print("metodo multi pop con 3 como parametro")
print("lista retornante",pila.multi_pop(3))

print("===="*23)
print("intercambia el tope con el ultimo")
pila.exchange()
print(pila)

print("===="*23)
print("reemplaza todos las apariciones del 5 con 89")
pila.replace_all(5,89)
print(pila)
