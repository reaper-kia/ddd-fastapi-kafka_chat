from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from app.domain.eventes.base import BaseEvent

ET = TypeVar('ET', bound=BaseEvent)
ER = TypeVar('ER', bound=Any) #результаты event_handler ов

@dataclass
class EventHandler(ABC, Generic[ET, ER]):
   @abstractmethod
   def handle(self, event: ET) -> ER:
      ...