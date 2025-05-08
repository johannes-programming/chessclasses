import enum

__all__ = ["File"]

class File(enum.IntEnum):

    (A, B, C, D, E, F, G, H) = range(8)

    def flip(self):
        "This method flips the players."
        return self

    
