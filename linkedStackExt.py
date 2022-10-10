from logging import raiseExceptions
from types import NoneType
from python_ed_fcad_uner.data_structures.linear.list_node import ListNode
from python_ed_fcad_uner.data_structures.linear.stacks.linked_stack import LinkedStack
from linkedStackExtAbstract import LinkedStackExtAbstract
from typing import Any, List


class LinkedStackExt(LinkedStackExtAbstract,LinkedStack):
    
   def multi_pop(self, num: int) -> List[Any]:
      if self.is_empty():
         raise Exception("estructura vacia, operacion no soportada")
      lista=[]
      i=0
      while i<num:
         lista.append(self.pop())
         i+=1
      return lista
   
   def replace_all(self, param1: Any, param2: Any) -> None:
         actual=self._head
         while actual:
          if actual.element.__eq__(param1):
             actual.element=param2
          actual=actual.next

   def exchange(self) -> None:
      if self.is_empty():
         raise Exception("estructura vacia, operacion no soportada")
      actual=self._head
      primero=self._head.element
      while actual:
          ultimo=actual.element
          if(actual.next==None):
            actual.element=primero
          actual=actual.next
      self._head.element=ultimo  
      

        

