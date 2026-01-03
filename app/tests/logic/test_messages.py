import pytest

from faker import Faker

from app.infra.repositories.messages.base import BaseChatRepository
from app.logic.exception.messages import ChatWithThatTitleAlreadyExistsException
from app.domain.exception.messages import TextToLongException
from app.domain.values.messages import Title
from app.domain.entities.messages import Chat

from app.logic.commands.messages import CreateChatCommand
from app.logic.mediator import Mediator

@pytest.mark.asyncio
async def test_create_chat_commands_success(
    chat_repository : BaseChatRepository,
    mediator : Mediator,
    faker : Faker
):
    
    chat: Chat
    chat, *_ = await mediator.handler_commands(CreateChatCommand(title=faker.text(max_nb_chars=100)))
    
    assert await chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())
    
@pytest.mark.asyncio
async def test_create_chat_commands_title_already_exists(
    chat_repository : BaseChatRepository,
    mediator : Mediator,
    faker : Faker
):
    #TODO закинуть фейкер
    title_text = faker.text(max_nb_chars=100)
    chat = Chat(title=Title(title_text))
    
    await chat_repository.add_chat(chat)
    
    assert chat in chat_repository._saved_chats
    
    with pytest.raises(ChatWithThatTitleAlreadyExistsException):
        await mediator.handler_commands(CreateChatCommand(title=title_text))
    
    assert len(chat_repository._saved_chats) == 1