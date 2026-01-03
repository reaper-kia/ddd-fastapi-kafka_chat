from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from app.logic.init import init_container
from app.tests.fixture import init_dumy_container
from app.application.api.main import create_app


@pytest.fixture
def app() -> FastAPI:
   app = create_app()
   app.dependency_overrides[init_container] = init_dumy_container
   
   return app

@pytest.fixture
def client(app: FastAPI) -> TestClient:
   return TestClient(app=app)