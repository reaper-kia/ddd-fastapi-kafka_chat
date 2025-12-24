from app.infra.repositories.messages import BaseChatRepository, MemoryChatRepository
from app.logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from app.logic.mediator import Mediator


def init_mediator(mediator: Mediator, chat_repository: BaseChatRepository):
    print(f"init_mediator called with chat_repository id: {id(chat_repository)}")
    
    from app.logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
    
    handler = CreateChatCommandHandler(chat_repository=chat_repository)
    
    print(f"Handler created with chat_repository id: {id(handler.chat_repository)}")
    
    # ВАЖНО: передаем как список
    mediator.register_command(CreateChatCommand, [handler])