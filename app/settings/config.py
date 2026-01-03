from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Config(BaseSettings):
   mongodb_connection_uri: str = Field(default="mongodb://localhost:27017", alias="MONGO_DB_CONNECTION_URI")
   mongodb_chat_database: str = Field(default="Chat", alias="MONGODB_CHAT_DATABASE")
   mongodb_chat_collection: str = Field(default="chat", alias="MONGODB_CHAT_COLLECTION")
    
   model_config = SettingsConfigDict(
      env_file=".env",
      env_file_encoding="utf-8",
      case_sensitive=False,
      extra="ignore"
   )