from deque import Deque

estruc=Deque()
i=0
while i<10:
    estruc.add_first(i)
    i+=1

print("===="*23)
print("estructura completa")
print(str(estruc))
print("===="*23)
print("agrego un elemento(22) al final de la estructura")
estruc.add_last(22)
print("===="*23)
print("agrego un elemento(76) al principio de la estructura")
estruc.add_first(76)
print(str(estruc))
print("===="*23)
print("borra el primer elemento de la estructura")
estruc.delete_first()
print(str(estruc))
print("===="*23)
print("borra el ultimo elemento de la estructura")
estruc.delete_last()
print(str(estruc))
print("===="*23)
print("devuelve el primer elemento de la estructura")
print(estruc.first())
print("===="*23)
print("devuelve el ultimo elemento de la estructura")
print(estruc.last())