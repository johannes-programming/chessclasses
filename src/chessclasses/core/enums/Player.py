import enum
from __future__ import annotations
from typing import *

__all__ = ["Player"]

class Player(enum.IntEnum):
    WHITE = 0
    BLACK = 1
    def flip(self) -> Self:
        "This method flips the players."
        return type(self)(1 - self)
    
