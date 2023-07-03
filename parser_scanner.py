import re
from tokens_scanner import Scanner
from tokens import TokenType


R_CHARS_URL = f"[#|-|_|:|&|?|=|/|.]"
R_PROTOCOLS = f"(http|https|ftp|ftps)://"
R_DOMAIN = f"([a-z]|[A-Z]|[0-9])+([.]|[a-z]|[A-Z]|[0-9])*"
R_PORT = f":(\d)+"
R_ROUTE = f"/([a-z]|[A-Z]|[.]|/?)*"
R_FRAGMENT = f"#([a-z]|[A-Z]|[0-9]|{R_CHARS_URL})+"

R_URL = f"{R_PROTOCOLS}({R_DOMAIN})({R_PORT})?({R_ROUTE})?({R_FRAGMENT})?"


class RegularExpression:
    def __init__(self):
        self.PROG = f"^\s{str(TokenType.DOCTYPE)}\s+{str(TokenType.ARTICLE_OPEN)}\s+({self.STRUCTURE})*\s+{str(TokenType.ARTICLE_CLOSE)}\s$"
        self.STRUCTURE = f"\s({self.INFO})?\s+({self.TITLE})?\s+{self.DOWN}\s"
        self.INFO = f"^\s{str(TokenType.INFO_OPEN)}\s+({mediaobject}\s+{self.AUTHOR}\s+{abstract}\s+{address}\s+{self.COPYRIGHT}\s+{self.DATE})+\s+{self.TITLE}{str(TokenType.INFO_CLOSE)}\s$"
        self.ELEMENTS = f"\s({itemizedlist}|{important}|{para}|{simpara}|{address}|{mediaobject}|{informaltable}|{comment}|{abstract})+"
        self.SECTION = f"\s{str(TokenType.SECTION_OPEN)}\s+{self.STRUCTURE}\s+{str(TokenType.SECTION_CLOSE)}\s"
        self.DOWN = f"\s({self.ELEMENTS})|({self.ELEMENTS}|{self.SECTION})\s"
        abstract = f"\s{str(TokenType.ABSTRACT_OPEN)}\s+({self.TITLE})?\s+({para}|{simpara})+\s+{str(TokenType.ABSTRACT_CLOSE)}\s+"
        mediaobject = f"\s{str(TokenType.MEDIAOBJECT_OPEN)}\s+(({self.INFO}\s)?({self.VIDEOOBJECT}|{self.IMAGEOBJECT})*)\s+{str(TokenType.MEDIAOBJECT_CLOSE)}\s"
        address = f"\s{str(TokenType.ADDRESS_OPEN)}\s+({self.TEXTO}|{self.STREET}|{self.CITY}|{self.STATE}|{self.PHONE}|{self.EMAIL})*\s+{str(TokenType.ADDRESS_CLOSE)}\s$"
        self.TITLE = f"\s{str(TokenType.TITLE_OPEN)}\s+{str(TokenType.TEXT)}\s+{str(TokenType.TITLE_CLOSE)}\s"
        self.AUTHOR = f"\s{str(TokenType.AUTHOR_OPEN)}\s+({self.FIRSTNAME}|{self.SURNAME})+\s+{str(TokenType.AUTHOR_CLOSE)}\s$"
        self.DATE = f"\s{str(TokenType.DATE_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.DATE_CLOSE)}\s+"
        self.COPYRIGHT = f"\s{str(TokenType.COPYRIGHT_OPEN)}\s+{self.YEAR}\s+{self.HOLDER}\s+{str(TokenType.COPYRIGHT_CLOSE)}\s$"
        self.EMAIL = f"\s{str(TokenType.EMAIL_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.EMAIL_CLOSE)}\s+"
        self.SIMPLE_SECTION = f"\s{str(TokenType.SIMP_SECTION_OPEN)}\s+(({self.INFO}\s{self.ELEMENTS})|({self.TITLE}\s+{self.ELEMENTS})|({self.ELEMENTS}))\s+{str(TokenType.SIMP_SECTION_CLOSE)}\s"
        important = f"\s{str(TokenType.IMPORTANT_OPEN)}\s+({self.TITLE})?\s+({itemizedlist}|{important}|{para}|{simpara}|{address}|{mediaobject}|{informaltable}|{comment}|{abstract})+\s+{str(TokenType. IMPORTANT_CLOSE)}\s+"
        para = f"\s{str(TokenType.PARA_OPEN)}\s+({str(TokenType.TEXT)}|{self.EMPHASIS}|{self.LINK}|{self.EMAIL}|{self.AUTHOR}|{comment}|{self.TEMIZEDLIST}|{important}|{address}{mediaobject}{informaltable})+\s{str(TokenType.PARA_CLOSE)}\s"
        itemizedlist = f"\s{str(TokenType.ITEMIZEDLIST_OPEN)}\s+({self.TITLE})?\s+({itemizedlist}|{important}|{para}|{simpara}|{address}|{mediaobject}|{informaltable}|{comment}|{abstract})+\s+{str(TokenType.ITEMIZEDLIST_CLOSE)}\s+"
        comment = f"\s{str(TokenType.COMMENT_OPEN)}\s+{self.OPC_1}\s+{str(TokenType.COMMENT_CLOSE)}\s$"
        simpara = f"\s{str(TokenType.SIMPARA_OPEN)}\s+{self.OPC_1}\s+{str(TokenType.SIMPARA_CLOSE)}\s$"
        self.EMPHASIS = f"\s{str(TokenType.EMPHASIS_OPEN)}\s+{self.OPC_1}\ s+{str(TokenType.EMPHASIS_CLOSE)}\s$"
        self.OPC_1 = f"({self.TEXTO}|{self.EMPHASIS}|{self.LINK}|{self.EMAIL}|{self.AUTHOR}|{comment})+"
        self.LISTITEM = f"\s{str(TokenType.LISTITEM_OPEN)}\s+({self.TITLE})?\s+({important}|{para}|{simpara}|{address}|{mediaobject}|{informaltable}|{comment}|{abstract})+\s+{str(TokenType.LISTITEM_CLOSE)}\s+"
        self.VIDEOOBJECT = f"{str(TokenType.VIDEOOBJECT_OPEN)}\s+(({self.INFO}\s)?{str(TokenType.VIDEODATA)})\s+{str(TokenType.VIDEOOBJECT_CLOSE)}\s"
        self.IMAGEOBJECT = f"{str(TokenType.IMAGEOOBJECT_OPEN)}\s(({self.INFO}\s)?{str(TokenType.IMAGEDATA)})\s+{str(TokenType.IMAGEOOBJECT_CLOSE)}\s"
        self.TGROUP = f"\s{str(TokenType.TGROUP_OPEN)}\s+({self.THEAD}|{self.TFOOT})?+\s({self.TBODY})\s+{str(TokenType.TGROUP_CLOSE)}\s+"
        self.TBODY = f"\s{str(TokenType.TBODY_OPEN)}\s+{self.ROW}\s+{str(TokenType.TBODY_CLOSE)}\s"
        self.TFOOT = f"\s{str(TokenType.TFOOT_OPEN)}\s+{self.ROW}\s+{str(TokenType.TFOOT_CLOSE)}\s"
        self.THEAD = f"\s{str(TokenType.THEAD_OPEN)}\s+{self.ROW}\s+{str(TokenType.THEAD_CLOSE)}\s"
        self.ROW = f"\s{str(TokenType.ROW_OPEN)}\s+({self.ENTRY}|{self.ENTRYBL})+\s+{str(TokenType.ROW_CLOSE)}\s+"
        self.ENTRYBL = f"\s{str(TokenType.ENTRYBL_OPEN)}\s+(({self.THEAD}\s)?{self.TBODY}\s+{str(TokenType.ENTRYBL_CLOSE)}\s"
        self.ENTRY = f"\s{str(TokenType.ENTRY_OPEN)}\s({self.TEXTO}|{itemizedlist}|{important}|{para}|{simpara}|{mediaobject}|{comment}|{abstract})+\s+{str(TokenType.ENTRY_CLOSE)}\s"
        informaltable = f"\s{str(TokenType.INFORMALTABLE_OPEN)}\s({mediaobject}+|{self.TGROUP}+)\s+{str(TokenType.INFORMALTABLE_CLOSE)}\s"
        self.FIRSTNAME = f"\s{str(TokenType.FIRSTNAME_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.FIRSTNAME_CLOSE)}\s+"
        self.SURNAME = f"\s{str(TokenType.SURNAME_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.SURNAME_CLOSE)}\s+"
        self.YEAR = f"\s{str(TokenType.YEAR_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.YEAR_CLOSE)}\s+"
        self.HOLDER = f"\s{str(TokenType.HOLDER_OPEN)}\s+({self.TEXTO}|self.{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.HOLDER_CLOSE)}\s+"
        self.LINK = f"\s{str(TokenType.LINK)}"
        self.STREET = f"\s{str(TokenType.STREET_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.STREET_CLOSE)}\s+"
        self.CITY = f"\s{str(TokenType.CITY_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.CITY_CLOSE)}\s+"
        self.STATE = f"\s{str(TokenType.STATE_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.STATE_CLOSE)}\s+"
        self.PHONE = f"\s{str(TokenType.FIRSTNAME_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{comment})+\s+{str(TokenType.FIRSTNAME_CLOSE)}\s+"
        self.TEXTO = f"([a-zA-Z][0-9])+"


class ParserScanner:
    def __init__(self, text) -> None:
        self.curr = None
        self.scanner = Scanner(text)
        self.advance()

    def advance(self):
        self.curr = self.scanner.scan()

    def parse(self, input):
        rule = RegularExpression()
        analize = re.fullmatch(rule.PROG, input)
        print(analize)
        while self.curr is not None:
            print(self.curr)
            self.advance()
            input()
