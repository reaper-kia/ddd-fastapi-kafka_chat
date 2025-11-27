from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.messages import Text, Title

@dataclass
class Message(BaseEntity):
   text: Text = field(kw_only=True)
   
   __hash__ = BaseEntity.__hash__


@dataclass
class Chat(BaseEntity):
   title : Title = field(kw_only=True)
   
   messages : set[Message] = field(
      default_factory= set,
      kw_only=True,
   )
   
   def add_message(self, message : Message):
      self.messages.add(message)
      
   __hash__ = BaseEntity.__hash__
   