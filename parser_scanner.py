from tokens_scanner import Scanner
from tokens import TokenType

reservadas = [
    "PROG",
    "STRUCTURE",
    "DOWN",
    "INT_INFO",
    "INT_TITLE",
    "ELEMENTS",
    "SECTIONS",
    "INT_SIMPLE_SEC",
    "INT_ABSTRACT",
    "INT_ADDRESS",
    "INT_AUTHOR",
    "INT_COPYRIGHT",
    "OPC_1",
    "INT_MEDIAOBJECT",
    "OPC_2",
    "INT_PARA",
]


R_CHARS_URL = f"[#|-|_|:|&|?|=|/|.]"
R_PROTOCOLS = f"(http|https|ftp|ftps)://"
R_DOMAIN = f"([a-z]|[A-Z]|[0-9])+([.]|[a-z]|[A-Z]|[0-9])*"
R_PORT = f":(\d)+"
R_ROUTE = f"/([a-z]|[A-Z]|[.]|/?)*"
R_FRAGMENT = f"#([a-z]|[A-Z]|[0-9]|{R_CHARS_URL})+"

R_URL = f"{R_PROTOCOLS}({R_DOMAIN})({R_PORT})?({R_ROUTE})?({R_FRAGMENT})?"

TEXTO = f'([a-zA-Z]+|ñ+|[0-9]+|\-|_|\#|&|\(|\)|\?|\¿|!|¡|\,|\=|\.|/+|"|;|:|\+)+'

ROW = f"\s{str(TokenType.ROW_OPEN)}\s+({ENTRY}|{ENTRYBL})+\s+{str(TokenType.ROW_CLOSE)}\s+"
TBODY = f"\s{str(TokenType.TBODY_OPEN)}\s+{ROW}\s+{str(TokenType.TBODY_CLOSE)}\s"
TFOOT = f"\s{str(TokenType.TFOOT_OPEN)}\s+{ROW}\s+{str(TokenType.TFOOT_CLOSE)}\s"
THEAD = f"\s{str(TokenType.THEAD_OPEN)}\s+{ROW}\s+{str(TokenType.THEAD_CLOSE)}\s"
TGROUP = f"\s{str(TokenType.TGROUP_OPEN)}\s+({THEAD}|{TFOOT})?+\s({TBODY})\s+{str(TokenType.TGROUP_CLOSE)}\s+"
ENTRYBL = f"\s{str(TokenType.ENTRYBL_OPEN)}\s+(({THEAD}\s)?{TBODY}\s+{str(TokenType.ENTRYBL_CLOSE)}\s"
ENTRY = f"\s{str(TokenType.ENTRY_OPEN)}\s({TEXTO}|{ITEMIZEDLIST}|{IMPORTANT}|{PARA}|{SIMPARA}|{MEDIAOBJECT}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType.ENTRY_CLOSE)}\s"

LINK = f"\s{str(TokenType.LINK)}"
FIRSTNAME = f"\s{str(TokenType.FIRSTNAME_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.FIRSTNAME_CLOSE)}\s+"
SURNAME = f"\s{str(TokenType.SURNAME_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.SURNAME_CLOSE)}\s+"
STREET = f"\s{str(TokenType.STREET_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.STREET_CLOSE)}\s+"
CITY = f"\s{str(TokenType.CITY_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.CITY_CLOSE)}\s+"
STATE = f"\s{str(TokenType.STATE_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.STATE_CLOSE)}\s+"
PHONE = f"\s{str(TokenType.FIRSTNAME_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.FIRSTNAME_CLOSE)}\s+"


YEAR = f"\s{str(TokenType.YEAR_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.YEAR_CLOSE)}\s+"
HOLDER = f"\s{str(TokenType.HOLDER_OPEN)}\s+({TEXTO}|{LINK}|{EMPHASIS}|{COMMENT})+\s+{str(TokenType.HOLDER_CLOSE)}\s+"


OPC_1 = f"({TEXTO}|{EMPHASIS}|{LINK}|{EMAIL}|{AUTHOR}|{COMMENT})+"
COMMENT = (
    f"\s{str(TokenType.COMMENT_OPEN)}\s+{OPC_1}\s+{str(TokenType.COMMENT_CLOSE)}\s$"
)
EMPHASIS = (
    f"\s{str(TokenType.EMPHASIS_OPEN)}\s+{OPC_1}\ s+{str(TokenType.EMPHASIS_CLOSE)}\s$"
)
SIMPARA = (
    f"\s{str(TokenType.SIMPARA_OPEN)}\s+{OPC_1}\s+{str(TokenType.SIMPARA_CLOSE)}\s$"
)

ITEMIZEDLIST_A = f"\s{str(TokenType.ITEMIZEDLIST_OPEN)}\s+({TITLE})?\s+({IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABLE}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType.ITEMIZEDLIST_CLOSE)}\s+"
LISTITEM = f"\s{str(TokenType.LISTITEM_OPEN)}\s+({TITLE})?\s+({IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABL}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType.LISTITEM_CLOSE)}\s+"
IMPORTANT = f"\s{str(TokenType.IMPORTANT_OPEN)}\s+({TITLE})?\s+({IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABLE}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType. IMPORTANT_CLOSE)}\s+"

ITEMIZEDLIST = f"\s{str(TokenType.ITEMIZEDLIST_OPEN)}\s+({TITLE})?\s+({ITEMIZEDLIST_A}|{IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABLE}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType.ITEMIZEDLIST_CLOSE)}\s+"
LISTITEM = f"\s{str(TokenType.LISTITEM_OPEN)}\s+({TITLE})?\s+({ITEMIZEDLIST_A}|{IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABL}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType.LISTITEM_CLOSE)}\s+"
IMPORTANT = f"\s{str(TokenType.IMPORTANT_OPEN)}\s+({TITLE})?\s+({ITEMIZEDLIST_A}|{IMPORTANT}|{PARA}|{SIMPARA}|{ADDRESS}|{MEDIAOBJECT}|{INFORMALTABLE}|{COMMENT}|{ABSTRACT})+\s+{str(TokenType. IMPORTANT_CLOSE)}\s+"

IMAGEOBJECT = f"{str(TokenType.IMAGEOOBJECT_OPEN)}\s(({INFO}\s)?{str(TokenType.IMAGEDATA)})\s+{str(TokenType.IMAGEOOBJECT_CLOSE)}\s"

VIDEOOBJECT = f"{str(TokenType.VIDEOOBJECT_OPEN)}\s+(({INFO}\s)?{str(TokenType.VIDEODATA)})\s+{str(TokenType.VIDEOOBJECT_CLOSE)}\s"

INFORMALTABLE = f"\s{str(TokenType.INFORMALTABLE_OPEN)}\s({MEDIAOBJECT}+|{TGROUP}+)\s+{str(TokenType.INFORMALTABLE_CLOSE)}\s"

PARA = f"\s{str(TokenType.PARA_OPEN)}\s+({str(TokenType.TEXT)}|{EMPHASIS}|{LINK}|{EMAIL}|{AUTHOR}|{COMMENT}|{ITEMIZEDLIST}|{IMPORTANT}|{ADDRESS}{MEDIAOBJECT}{INFORMALTABLE})+\s{str(TokenType.PARA_CLOSE)}\s"


class RegularExpression:
    def __init__(self):
        self.PROG = f"^\s{str(TokenType.DOCTYPE)}\s+{str(TokenType.ARTICLE_OPEN)}\s+({self.STRUCTURE})*\s+{str(TokenType.ARTICLE_CLOSE)}\s$"
        self.STRUCTURE = f"\s({self.INFO})?\s+({self.TITLE})?\s+{self.DOWN}\s"
        self.INFO = f"^\s{str(TokenType.INFO_OPEN)}\s+({self.MEDIAOBJECT}\s+{self.AUTHOR}\s+{self.ABSTRACT}\s+{self.ADDRESS}\s+{self.COPYRIGHT}\s+{self.DATE})+\s+{self.TITLE}{str(TokenType.INFO_CLOSE)}\s$"
        self.ELEMENTS = f"\s({self.ITEMIZEDLIST}|{self.IMPORTANT}|{self.PARA}|{self.SIMPARA}|{self.ADDRESS}|{self.MEDIAOBJECT}|{self.INFORMALTABLE}|{self.COMMENT}|{self.ABSTRACT})+"
        self.SECTION = f"\s{str(TokenType.SECTION_OPEN)}\s+{self.STRUCTURE}\s+{str(TokenType.SECTION_CLOSE)}\s"
        self.DOWN = f"\s({self.ELEMENTS})|({self.ELEMENTS}|{self.SECTION})\s"
        self.ABSTRACT = f"\s{str(TokenType.ABSTRACT_OPEN)}\s+({self.TITLE})?\s+({self.PARA}|{self.SIMPARA})+\s+{str(TokenType.ABSTRACT_CLOSE)}\s+"
        self.MEDIAOBJECT = f"\s{str(TokenType.MEDIAOBJECT_OPEN)}\s+(({self.INFO}\s)?({self.VIDEOOBJECT}|{self.IMAGEOBJECT})*)\s+{str(TokenType.MEDIAOBJECT_CLOSE)}\s"
        self.ADDRESS = f"\s{str(TokenType.ADDRESS_OPEN)}\s+({self.TEXTO}|{self.STREET}|{self.CITY}|{self.STATE}|{self.PHONE}|{self.EMAIL})*\s+{str(TokenType.ADDRESS_CLOSE)}\s$"
        self.TITLE = f"\s{str(TokenType.TITLE_OPEN)}\s+{str(TokenType.TEXT)}\s+{str(TokenType.TITLE_CLOSE)}\s"
        self.AUTHOR = f"\s{str(TokenType.AUTHOR_OPEN)}\s+({self.FIRSTNAME}|{self.SURNAME})+\s+{str(TokenType.AUTHOR_CLOSE)}\s$"
        self.DATE = f"\s{str(TokenType.DATE_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{self.COMMENT})+\s+{str(TokenType.DATE_CLOSE)}\s+"
        self.COPYRIGHT = f"\s{str(TokenType.COPYRIGHT_OPEN)}\s+{self.YEAR}\s+{self.HOLDER}\s+{str(TokenType.COPYRIGHT_CLOSE)}\s$"
        self.EMAIL = f"\s{str(TokenType.EMAIL_OPEN)}\s+({self.TEXTO}|{self.LINK}|{self.EMPHASIS}|{self.COMMENT})+\s+{str(TokenType.EMAIL_CLOSE)}\s+"
        self.SIMPLE_SECTION = f"\s{str(TokenType.SIMP_SECTION_OPEN)}\s+(({self.INFO}\s{self.ELEMENTS})|({self.TITLE}\s+{self.ELEMENTS})|({self.ELEMENTS}))\s+{str(TokenType.SIMP_SECTION_CLOSE)}\s"


class ParserScanner:
    def __init__(self, text) -> None:
        self.curr = None
        self.scanner = Scanner(text)
        self.advance()

    def advance(self):
        self.curr = self.scanner.scan()

    def parse(self):
        while self.curr is not None:
            print(self.curr)
            self.advance()
            input()


text = """  <!DOCTYPE article>
            <article>
                <info>
                <title>El titulo del articulo</title>
                <author>
                    <firstname>Juan</firstname>
                    <surname>Perez</surname>
                </author>
                <para></para>
                <para></para>
                <para></para>
                <para></para>
            </article>"""

parser = ParserScanner(text)
parser.parse()
