from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

VT = TypeVar('VT', bound=any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]): #generic самостоятельно определяет тип данных
   value: VT
   
   def __post_init__(self):
      self.validate()
   
   def __eq__(self, value):
      return super().__eq__(value)
   
   @abstractclassmethod
   def validate(self):
      ...
      
   @abstractclassmethod
   def as_generic_type(self) -> VT:
      ...