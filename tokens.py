from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    DOCTYPE = '<!DOCTYPE article>' # if <!DOCTYPE !endsWith('>')
    ARTICLE_O = '<article>'
    ARTICLE_C = '</article>'
    INFO_O = '<info>'
    INFO_C = '</info>'
    TITLE_O = '<title>'
    TITLE_C = '</title>'
    SIMP_SECTION_O = '<s>'
    LABRACKET = '<'
    RABRACKET = '>'
    
    def __str__(self) -> str:
        return self.name
    
@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    
    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'