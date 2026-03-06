from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_config(path: str | None = None) -> Config:
    Token = os.getenv('Token')
    return Config(
        bot=TgBot(token=Token))