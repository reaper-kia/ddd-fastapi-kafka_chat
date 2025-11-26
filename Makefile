# Определение переменных
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker-compose.yml
APP_CONTAINER = main-app-new
STORAGES_FILE = docker-compose/storages.yaml

# Задачи для сборки и запуска контейнеров

.PHONY: app
app:
	$(DC) -f $(APP_FILE) $(ENV) up --build -d

.PHONY: app-down
app-down:
	$(DC) -f $(APP_FILE) down

.PHONY: app-shell
app-shell:
	$(EXEC) $(APP_CONTAINER) bash

.PHONY: app-logs
app-logs:
	$(LOGS) $(APP_CONTAINER) -f
