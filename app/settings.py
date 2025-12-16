from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "email-addon-api"
    environment: str = "local"
    log_level: str = "INFO"

    # Optional: shared secret for simple local protection (set to empty to disable)
    api_key: str = ""


settings = Settings()
