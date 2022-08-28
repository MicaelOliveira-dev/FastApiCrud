from unittest.util import strclass
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    frase: str
    autor: str