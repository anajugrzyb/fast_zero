from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='C:/Users/grzyb/OneDrive/Documentos/projetos/fast_zero/.env',
        env_file_encoding='utf-8',
    )

    DATABASE_URL: str
