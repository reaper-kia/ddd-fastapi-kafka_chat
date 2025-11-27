from datetime import datetime
import pytest 

from app.domain.exception.messages import TextToLongException
from app.domain.values.messages import Text, Title
from app.domain.entities.messages import Chat, Message

def test_create_message_success():
   text = Text('hello')
   message = Message(text=text)
   
   assert message.text == text
   assert message.created_at.date() == datetime.today().date()

def test_create_message_text_to_long():
   with pytest.raises(TextToLongException):
      text = Text('3' * 400)

def test_create_chat_success():
   title = Title('Title')
   chat = Chat(title=title)
   
   assert chat.title == title
   assert not chat.messages
   assert chat.created_at.date() == datetime.today().date()

def test_create_message_title_to_long():
   with pytest.raises(TextToLongException):
      Title('3' * 400)

def test_add_chat_to_message():
   text = Text('hello')
   message = Message(text=text)
   
   title = Title('Title')
   chat = Chat(title=title)
   
   chat.add_message(message=message)
   
   assert message in chat.messages