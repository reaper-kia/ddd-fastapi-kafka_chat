from fastapi import FastAPI

from app.application.api.messages.handlers import router as chat_router

def create_app() -> FastAPI:
   app = FastAPI(
      title="Kafka chat",
      docs_url="/api/docs",
      description="simple kafka",
      debug=True,
   )
   app.include_router(chat_router, prefix='/chat')
   return app

