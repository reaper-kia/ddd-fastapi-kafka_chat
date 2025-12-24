from dataclasses import dataclass

from app.domain.eventes.base import BaseEvent

@dataclass 
class NewMessageRecivedEvent(BaseEvent):
   message_text : str
   message_oid : str
   chat_oid : str
   
@dataclass
class NewChatCreated(BaseEvent):
   chat_oid : str
   chat_title : str