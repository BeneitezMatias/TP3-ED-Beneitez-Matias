from nodolistadoble import NodolistaDoble
from doubleLinkedListAbstract import DoubleLinkedListAbstract
from typing import Any, Iterator

class DoubleLinkedList(DoubleLinkedListAbstract):
    
    def __init__(self) -> None:
        self._header:NodolistaDoble = NodolistaDoble(None,None,None)
        self._size:int=0
    
    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, key: int) -> Any:
        if key>self._size or key<1:
            raise Exception("indice fuera de rango")
        else:
            i=1
            actual=self._header.next
            while actual:
                if(i == key):
                    elemento=actual.element
                    break
                i+=1
                actual=actual.next
            return elemento
 
    def __setitem__(self, key: int, value: Any) -> None:
        if key>self._size or key<1:
            raise Exception("indice fuera de rango")
        else:
            i=1
            actual=self._header.next
            while actual:
                if(i == key):
                    actual.element=value
                    break
                i+=1
                actual=actual.next
    
    def __delitem__(self, key: int) -> None:
        if key>self._size or key<1:
            raise Exception("indice fuera de rango")
        else:
            i=1
            actual=self._header.next
            while actual:
                if(i == key):
                    Nodoanterior=actual.anterior
                    Nodosiguiente=actual.next
                    Nodoanterior.next=Nodosiguiente
                    Nodosiguiente.anterior=Nodoanterior
                    break
                i+=1
                actual=actual.next
            self._size-=1
    
    def __iter__(self) -> Iterator[Any]:
         pass
    
    def __str__(self) -> str:
       if self.is_empty():
            return "DoubleLinkedList()"  
       res="" 
       actual = self._header.next 
       while actual:
        res += str(actual.element) + ", "
        actual = actual.next  
       res = res[:-2]
       return f"DoubleLinkedList({res})"
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def append(self, elem: Any) -> None:
        nuevo=NodolistaDoble(elem)
        if self.is_empty():
            self._header.next=nuevo
            nuevo.anterior=self._header
        else:
            actual=self._header.next
            while actual:
                if actual.next==None:
                    actual.next=nuevo
                    nuevo.anterior=actual
                    break
                actual=actual.next
        self._size+=1

