from tokens_scanner import Scanner


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


text = """<!DOCTYPE article><article><info><title>El titulo del articulo</title><author><firstname>Juan</firstname><surname>Perez</surname></author></article>"""

parser = ParserScanner(text)
parser.parse()
