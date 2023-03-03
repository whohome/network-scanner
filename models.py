from pydantic import BaseModel


class Target(BaseModel):
    target: str
