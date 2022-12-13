import os

class environment:
    PROJECT_NAME: str = "Todo App"
    PROJECT_VERSION: str = "1.0.0"
    DEFAULT_DB_NAME: str = "tasks"
    DB_NAME: str = os.getenv("db", DEFAULT_DB_NAME)
    DB_HOST: str = "mongodb://todo-app-db"
    DEFAULT_DB_PORT: int = 27017
    DB_PORT: int = int(os.getenv("db_port",DEFAULT_DB_PORT))

settings = environment()