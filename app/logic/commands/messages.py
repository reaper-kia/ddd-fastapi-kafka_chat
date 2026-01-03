from dataclasses import dataclass

from app.domain.entities.messages import Chat
from app.domain.values.messages import Title
from app.infra.repositories.messages.base import BaseChatRepository
from app.logic.commands.base import BaseCommand, CommandHandler
from app.logic.exception.messages import ChatWithThatTitleAlreadyExistsException

@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
   title : str

@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
   chat_repository: BaseChatRepository

   async def handler(self, command: CreateChatCommand) -> Chat:
      # Проверка существования чата
      if await self.chat_repository.check_chat_exists_by_title(command.title):
         raise ChatWithThatTitleAlreadyExistsException(command.title)
      # Создание объекта Title
      title = Title(value=command.title)

      # Создание чата и регистрация события
      new_chat = Chat.create_chat(title=title)
      # Сохранение чата в репозитории
      await self.chat_repository.add_chat(new_chat)

      # Возврат созданного чата
      return new_chat