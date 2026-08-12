from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    bot_access_token: str

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str
    postgres_password: str
    postgres_db: str

    github_webhook_secret: str

    telegram_api_url: str


    @property
    def redis_url(self) -> str:
        return (
            f"redis://"
            f"{self.redis_host}:{self.redis_port}"
            f"/{self.redis_db}"
        )

    @property
    def postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )


settings = Settings() # type: ignore