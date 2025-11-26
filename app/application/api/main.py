from fastapi import FastAPI

def create_app():
   app = FastAPI(
      title="Kafka chat",
      docs_url="/api/docs",
      description="simple kafka",
      debug=True,
   )
   return app

app = create_app()