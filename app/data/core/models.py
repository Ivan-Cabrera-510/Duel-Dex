from dataclasses import dataclass, field
from typing import Optional

@dataclass
#Holds a reference to a card by its ID and name.
class CardRef:
    id: int
    name: str
    type: Optional[str] = None # The type of the card (e.g., Monster, Spell, Trap).
    race: Optional[str] = None # “Dragon”, “Fairy”, etc.
    attribute: Optional[str] = None # “Light”, “Dark”, etc.
    archetype: Optional[str] = None # The archetype the card belongs to, if any.
    level: Optional[int] = None # The level/rank of the card, if applicable.
    atk: Optional[int] = None # Attack points, if applicable.
    defen: Optional[int] = None # Defense points, if applicable.
    effect: Optional[str] = None # A brief description of the card's effect, if any.
    flags: set[str] = field(default_factory=set) # Additional flags or tags associated with the card. (banished or used for normal summon, etc.)
