from enum import Enum, auto 
from typing import Union

class Name(Enum):
    WIKIPEDIA = auto()
    GOOGLE = auto()
    NONE = auto()

    def __str__(self) -> str:       
     return self.name.lower()
    
Observation = Union[str , Exception]
    