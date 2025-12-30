from pydantic import BaseModel

from app.domain.entities.messages import Chat

class CreateChatRequestSchemas(BaseModel):
   title: str
   
class CreateChatResponseSchemas(BaseModel):
   oid: str
   title: str
   
   @classmethod
   def from_entity(cls, chat: Chat) -> 'CreateChatResponseSchemas':
      return CreateChatResponseSchemas(
         oid = chat.oid,
         title=chat.title.as_generic_type(),
      )