from dataclasses import dataclass

from app.logic.exception.base import LogicException

@dataclass(frozen=True, eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
   title : str
   
   @property
   def message(self):
      return f"Чат с таким названием {self.title} уже существует"