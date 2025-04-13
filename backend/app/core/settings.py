from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    A class to represent the settings of the application.

    Attributes:
        DB_URL (str): The URL of the database.
        DB_USER (str): The user of the database.
        DB_PASSWORD (str): The password of the database.
        DB_NAME (str): The name of the database.
        TEST_DB_URL (str): The URL of the test database.
    """

    DB_URL: str = Field(
        title="URL do banco de dados",
        description="URL do banco de dados",
        default="postgresql://user:password@localhost:5432/database",
    )
    DB_USER: str = Field(
        title="Usuário do banco de dados",
        description="Usuário do banco de dados",
        default="user",
    )
    DB_PASSWORD: str = Field(
        title="Senha do banco de dados",
        description="Senha do banco de dados",
        default="password",
    )
    DB_NAME: str = Field(
        title="Nome do banco de dados",
        description="Nome do banco de dados",
        default="database",
    )
    TEST_DB_URL: str = Field(
        title="URL do banco de dados de teste",
        description="URL do banco de dados de teste",
        default="sqlite+aiosqlite:///:memory:",
    )

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


config = Settings()
