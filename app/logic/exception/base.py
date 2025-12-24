from dataclasses import dataclass

from app.domain.exception.base import ApplicationException

@dataclass(frozen=True, eq=False)
class LogicException(ApplicationException):
   @property
   def message(self):
      return f"В обработке запроса возникли ошибки"