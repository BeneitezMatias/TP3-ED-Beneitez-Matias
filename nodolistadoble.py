from python_ed_fcad_uner.data_structures import ListNode
from typing import Any, Union

class NodolistaDoble:
    __slots__ = "element","next","anterior"
    def __init__(self, element: Any, next=None,anterior=None) -> None:
        self.element=element
        self.next: Union[NodolistaDoble,None]=next
        self.anterior: Union[NodolistaDoble,None]=anterior
    def __iter__(self):
        return iter(self.element)
 