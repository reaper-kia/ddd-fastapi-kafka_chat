from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from app.domain.entities.messages import Chat


@dataclass
class BaseChatRepository(ABC):
   @abstractmethod
   async def check_chat_exists_by_title(self, title: str):
      ...
   
   @abstractmethod
   async def add_chat(self, chat: Chat) -> None:
      ...
   
   # @abstractmethod
   # async def get_all_chats(self) -> List[Chat]:  # Добавьте этот метод
   #    ...