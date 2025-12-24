from dataclasses import dataclass, field

from app.domain.eventes.message import NewChatCreated, NewMessageRecivedEvent
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
   
   @classmethod
   def create_chat(cls, title: Title) -> "Chat":
    new_chat = cls(title=title)
    event = NewChatCreated(chat_oid=new_chat.oid, chat_title=new_chat.title)
    new_chat.register_event(event)
    return new_chat
   
   def add_message(self, message : Message):
      self.messages.add(message)
      self.register_event(NewMessageRecivedEvent(
         message_text=message.text.as_generic_type(),
         chat_oid = self.oid,
         message_oid = message.oid
      ))
      
   __hash__ = BaseEntity.__hash__
   