from dequeAbstract import DequeAbstract
from python_ed_fcad_uner.data_structures import LinkedList , ListNode
from typing import Any,List

class Deque(DequeAbstract,LinkedList):
 
 def __init__(self) -> None:
    super().__init__()
 
 def __len__(self) -> int:
    return self._size

 def __str__(self) -> str:
     if self.is_empty():
            return "Deque()"  
     res="" 
     actual = self._header.next 
     while actual:
        res += str(actual.element) + ", "
        actual = actual.next 
     res = res[:-2]
     return f"Deque({res})"
    
 def is_empty(self) -> bool:
     return self._size==0

 def first(self) -> Any:
    if self.is_empty():
      raise Exception("la estructura esta vacia")
    primero=self._header.next
    return primero.element

 def last(self) -> Any:
    if self.is_empty():
      raise Exception("la estructura esta vacia")
    else:
      actual=self._header.next
      while actual:
         if actual.next==None:
            return actual.element
         actual=actual.next

 def add_first(self, element : Any) -> None:
    nuevo=ListNode(element)
    if self.is_empty():
      self._header.next=nuevo
    else:
      primero=self._header.next
      nuevo.next=primero
      self._header.next=nuevo
    
    self._size+=1

 def add_last(self, element : Any) -> None:
    nuevo=ListNode(element)
    if self.is_empty():
      self._header.next=element
    else:
      actual=self._header.next
      while actual:
        if actual.next==None:
           actual.next=nuevo
           break
        actual=actual.next   
    self._size+=1

 def delete_first(self) -> None:
    if self.is_empty():
      raise Exception("la estructura esta vacia")
    else:
     primero=self._header.next
     self._header.next=primero.next

 def delete_last(self) -> None:
    if self.is_empty():
      raise Exception("la estructura esta vacia")
    else:
      actual=self._header.next
      while actual:
         siguiente=actual.next
         if(siguiente.next==None):
            actual.next=None
         actual=actual.next
            

