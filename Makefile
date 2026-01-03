# Определение переменных
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker-compose.yml
STORAGES_FILE = storages.yml
APP_CONTAINER = main-app-new

# Задачи для сборки и запуска контейнеров

.PHONY: app
app:
	$(DC) -f $(APP_FILE) $(ENV) up --build -d

.PHONY: storages
storages:
	$(DC) -f $(STORAGES_FILE) $(ENV) up --build -d

.PHONY: all
all:
	$(DC) -f $(STORAGES_FILE) -f $(APP_FILE) $(ENV) up --build -d


.PHONY: app-down
app-down:
	$(DC) -f $(APP_FILE) down

.PHONY: storages-down
storages-down:
	$(DC) -f $(STORAGES_FILE) down

.PHONY: app-shell
app-shell:
	$(EXEC) $(APP_CONTAINER) bash

.PHONY: app-logs
app-logs:
	$(LOGS) $(APP_CONTAINER) -f

.PHONY: test
test:
	$(EXEC) $(APP_CONTAINER) python -m pytest /app/app/tests/ -v

# .PHONY: copy-tests
# copy-tests:
# 	docker cp ./app/tests $(APP_CONTAINER):/app/app/tests

# .PHONY: fix-structure
# fix-structure:
# 	docker exec -it $(APP_CONTAINER) bash -c "if [ -d /app/app/app ]; then mv /app/app/app/* /app/ && rm -rf /app/app/app; fi"
# 	docker exec -it $(APP_CONTAINER) rm -rf /app/app/tests
# 	docker cp ./app/tests $(APP_CONTAINER):/app/app/

# .PHONY: test-clean
# test-clean: fix-structure
# 	$(EXEC) $(APP_CONTAINER) python -m pytest /app/app/tests/ -v

# .PHONY: debug-structure
# debug-structure:
# 	$(EXEC) $(APP_CONTAINER) find /app -name "*.py" -path "*/values/*" -type f