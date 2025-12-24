from dataclasses import dataclass

from app.logic.exception.base import LogicException

@dataclass(frozen=True, eq=False)
class EventHandlersNotRegisteredException(LogicException):
   event_type : type
   
   @property
   def message(self):
      return f"не удалось найти обработчика для события: {self.event_type}"
   
@dataclass(frozen=True, eq=False)
class CommandHandlersNotRegisteredException(LogicException):
   command_type : type
   
   @property
   def message(self):
      return f"не удалось найти обработчика для команды: {self.command_type}"