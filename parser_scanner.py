from tokens_scanner import Scanner
from tokens import TokenType

R_CHARS_URL = f"[#|-|_|:|&|?|=|/|.]"
R_PROTOCOLS = f"(http|https|ftp|ftps)://"
R_DOMAIN = f"([a-z]|[A-Z]|[0-9])+([.]|[a-z]|[A-Z]|[0-9])*"
R_PORT = f":(\d)+"
R_ROUTE = f"/([a-z]|[A-Z]|[.]|/?)*"
R_FRAGMENT = f"#([a-z]|[A-Z]|[0-9]|{R_CHARS_URL})+"

R_URL = f"{R_PROTOCOLS}({R_DOMAIN})({R_PORT})?({R_ROUTE})?({R_FRAGMENT})?"

STRUCTURE = f""

PROG = f"""^\s{str(TokenType.DOCTYPE)}\s+{str(TokenType.ARTICLE_OPEN)}\s+({STRUCTURE})*\s+{str(TokenType.ARTICLE_CLOSE)}\s$"""


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
