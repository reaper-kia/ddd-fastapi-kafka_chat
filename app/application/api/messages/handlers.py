from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from app.logic.init import init_container
from app.application.api.schemas import ErrorSchemas
from app.domain.exception.base import ApplicationException
from app.application.api.messages.shemas import CreateChatRequestSchemas, CreateChatResponseSchemas
from app.logic.commands.messages import CreateChatCommand
from app.logic.mediator import Mediator

router = APIRouter(
   tags=['Chat']
)

@router.post(
   '/', 
   response_model=CreateChatResponseSchemas, 
   status_code=status.HTTP_201_CREATED,
   description='Эндпоинт создает новый чат, если чат с таким названием существует, то ошибка 400',
   responses={
      status.HTTP_201_CREATED: {'model': CreateChatResponseSchemas},
      status.HTTP_400_BAD_REQUEST: {'model': ErrorSchemas},
   }
   )
async def create_chat_handler(schemas: CreateChatRequestSchemas, container=Depends(init_container)):
   """ Создать новый чат """
   mediator: Mediator = container.resolve(Mediator)
   
   try:
      chat, *_ = await mediator.handler_commands(CreateChatCommand(title=schemas.title))
   except ApplicationException as exception:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=({'erroe': exception.message}))
   
   return CreateChatResponseSchemas.from_entity(chat)