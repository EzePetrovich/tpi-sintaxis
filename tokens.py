from dataclasses import dataclass
from enum import Enum

class TokenWithUri:
    def __init__(self, init_name, end_name):
        self.init_name = init_name
        self.end_name = end_name if end_name else '"/>'
        
    def completeToken(self):
        return(self.init_name + self.end_name)

class TokenType(Enum):
    DOCTYPE = '<!doctype article>'
    ARTICLE_OPEN = '<article>'
    ARTICLE_CLOSE = '</article>'
    INFO_OPEN = '<info>'
    INFO_CLOSE = '</info>'
    TITLE_OPEN = '<title>'
    TITLE_CLOSE = '</title>'
    SIMP_SECTION_OPEN = '<simplesect>'
    SIMP_SECTION_CLOSE = '</simplesect>'
    SECTION_OPEN = '<section>'
    SECTION_CLOSE = '</section>'
    ABSTRACT_OPEN = '<abstract>'
    ABSTRACT_CLOSE = '</abstract>'
    ADDRESS_OPEN = '<address>'
    ADDRESS_CLOSE = '</address>'
    AUTHOR_OPEN = '<author>'
    AUTHOR_CLOSE = '</author>'
    COPYRIGHT_OPEN = '<copyright>'
    COPYRIGHT_CLOSE = '</copyright>'
    SIMPARA_OPEN = '<simpara>'
    SIMPARA_CLOSE = '</simpara>'
    EMPHASIS_OPEN = '<emphasis>'
    EMPHASIS_CLOSE = '</emphasis>'
    COMMENT_OPEN = '<comment>'
    COMMENT_CLOSE = '</comment>'
    IMPORTANT_OPEN = '<important>'
    IMPORTANT_CLOSE = '</important>'
    ITEMIZEDLIST_OPEN = '<itemizedlist>' 
    ITEMIZEDLIST_CLOSE = '</itemizedlist>'
    LISTITEM_OPEN = '<listitem>'
    LISTITEM_CLOSE = '</listitem>'
    PARA_OPEN = '<para>'
    PARA_CLOSE = '</para>'
    MEDIAOBJECT_OPEN = '<mediaobject>'
    MEDIAOBJECT_CLOSE = '</mediaobject>'
    VIDEOOBJECT_OPEN = '<videoobject>'
    VIDEOOBJECT_CLOSE = '</videoobject>'
    IMAGEOOBJECT_OPEN = '<imageobject>'
    IMAGEOOBJECT_CLOSE = '</imageobject>'
    FIRSTNAME_OPEN = '<firstname>'
    FIRSTNAME_CLOSE = '</firstname>'
    SURNAME_OPEN = '<surname>'
    SURNAME_CLOSE = '</surname>'
    STREET_OPEN = '<street>'
    STREET_CLOSE = '</street>'
    CITY_OPEN = '<city>'
    CITY_CLOSE = '</city>'
    STATE_OPEN = '<state>'
    STATE_CLOSE = '</state>'
    PHONE_OPEN = '<phone>'
    PHONE_CLOSE = '</phone>'
    EMAIL_OPEN = '<email>'
    EMAIL_CLOSE = '</email>'
    DATE_OPEN = '<date>'
    DATE_CLOSE = '</date>'
    YEAR_OPEN = '<year>'
    YEAR_CLOSE = '</year>'
    HOLDER_OPEN = '<holder>'
    HOLDER_CLOSE = '</holder>'
    INFORMALTABLE_OPEN = '<informaltable>'
    INFORMALTABLE_CLOSE = '</informaltable>'
    TGROUP_OPEN = '<tgroup>'
    TGROUP_CLOSE = '</tgroup>'
    THEAD_OPEN = '<thead>'
    THEAD_CLOSE = '</thead>'
    TFOOT_OPEN = '<tfoot>'
    TFOOT_CLOSE = '</tfoot>'
    TBODY_OPEN = '<tbody>'
    TBODY_CLOSE = '</tbody>'
    TEXT = '<text>'
    IMAGEDATA = TokenWithUri('<imagedata fileret="', None) 
    VIDEODATA = TokenWithUri('<videodata fileret="', None)
    LINK = TokenWithUri('<xlink:href:="', '">')
    
    def __str__(self) -> str:
        return self.name
    
@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    
    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'