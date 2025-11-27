from dataclasses import dataclass

from app.domain.exception.base import ApplicationException

@dataclass(frozen=True)
class TextToLongException(ApplicationException):
   text : str
   
   @property
   def message(self):
      return f"Error: very long text message {self.text[:255]}"

@dataclass(frozen=True)
class EmptyTextException(ApplicationException):
   
   @property
   def message(self):
      return "The message cannot be empty."