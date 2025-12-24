from copy import copy
from dataclasses import dataclass, field
from abc import ABC
from datetime import datetime
from uuid import uuid4

from app.domain.eventes.base import BaseEvent

@dataclass
class BaseEntity(ABC):
   oid: str = field(
      default_factory=lambda: str(uuid4())
      )
   
   created_at: datetime = field(
      default_factory=datetime.now, 
      kw_only=True
      )
   
   def __hash__(self):
      return hash(self.oid)
   
   def __eq__(self, __value: 'BaseEntity') -> bool:
      return self.oid == __value.oid
   
   _events : list[BaseEvent] = field(
      default_factory=list,
      kw_only=True
      )
   
   def register_event(self, event : BaseEvent) -> None:
      self._events.append(event)
   
   def pull_events(self):
      register_events = copy(self._events)
      self._events.clear()
      
      return register_events
   
   