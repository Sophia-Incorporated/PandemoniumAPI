from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Pandemonium API"
    database_url: str
    jwt_secret: str = "BibiErMegetSød"
    jwt_algorithm: str = "HS256"
    echo_sql: bool = True

settings = Settings()