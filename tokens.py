from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    TRUE = 1
    FALSE = 2
    AND = 3
    OR = 4
    NOT = 5
    LPAREN = 6
    RPAREN = 7
    
    def __str__(self) -> str:
        return self.name
    
@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    
    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'