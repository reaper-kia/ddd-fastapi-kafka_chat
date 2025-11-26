from dataclasses import dataclass

@dataclass(frozen=True)
class ApplicationException(Exception):
   @property
   def message(self):
      return "Application error occurred"