from tokens import Token, TokenType, TokenWithUri

PROTOCOLS = ["http://", "https://", "ftp://", "ftps://"]
CHARS_OK = ["#", "-", "_", ":", "&", "?", "=", "/", "."]


class ScannerURL:
    def __init__(self, url) -> None:
        self.url = url
        self.it = iter(url)
        self.curr = None
        self.isValid = True
        self.advance()

    def advance(self):
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None

    def okChars(self):
        while self.curr is not None:
            if self.curr.isdigit() or self.curr.isalpha() or self.curr in CHARS_OK:
                self.advance()
            else:
                self.isValid = False
                # print(f"La URL posee un caracter no válido -> {self.curr}")

    def validateUrl(self):
        match = False
        url_copy = self.url
        protocol_matched = ""
        for protocol in PROTOCOLS:
            match = match or (protocol in self.url)
            if match:
                protocol_matched = protocol
                break
        self.isValid = match
        # if not match:
        # print("La URL no tiene protocolo.")
        url_copy = url_copy.replace(protocol_matched, "")
        self.isValid = self.isValid and len(url_copy) > 0
        # print("La URL no tiene dominio.")

    def process(self):
        self.okChars()
        self.validateUrl()


class Scanner:
    def __init__(self, text) -> None:
        self.it = iter(text)
        self.curr = None
        self.line = 1
        self.lines_tokens = [dict(tokens=[], line=self.line)]
        self.advance()

    def advance(self):
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None

    def scan(self):
        scan_url = None
        tokens_values = [t.value for t in TokenType]
        tokens = [t for t in TokenType]
        tokens_with_uri = []
        url = ""
        content = ""

        for t in tokens:
            if isinstance(t.value, TokenWithUri):
                tokens_with_uri.append(t)

        while self.curr is not None:
            if self.curr in ("\n", "\t"):
                if self.curr == "\n":
                    if len(content) > 0:
                        content = ""
                        return Token(TokenType.TEXT, "<text>")
                    self.line += 1
                    self.lines_tokens.append(dict(tokens=[], line=self.line))
                self.advance()
            else:
                if self.curr == "<":
                    if len(content) > 0:
                        content = ""
                        return Token(TokenType.TEXT, "<text>")
                    word = self.getWord()
                    if tokens_with_uri:
                        for t_uri in tokens_with_uri:
                            if t_uri.value.init_name in word and word.endswith(
                                t_uri.value.end_name
                            ):
                                # url = word.replace(t_uri.value.init_name, "").replace(
                                #    t_uri.value.end_name, ""
                                # )

                                url = self.extractURL(
                                    word, t_uri.value.init_name, t_uri.value.end_name
                                )

                                scan_url = ScannerURL(url)
                                scan_url.process()
                                if scan_url.isValid:
                                    return self.getToken(
                                        t_uri.value.completeToken(None), tokens, url
                                    )
                        else:
                            if word in tokens_values:
                                return self.getToken(word, tokens, None)
                            else:
                                return word
                if self.curr != None and self.curr != "<":
                    if self.curr != ">":
                        content += self.curr
                    self.advance()
        if self.curr == None and len(content) > 0:
            content = ""
            return Token(TokenType.TEXT, "<text>")
        return None

    def scanAll(self):
        while True:
            token = self.scan()
            if token is None:
                break
            self.lines_tokens[self.line - 1]["tokens"].append(token)
        self.line = 0
        return self.lines_tokens

    def getWord(self) -> str:
        word = self.curr
        self.advance()
        while self.curr != ">" and self.curr != "<" and self.curr is not None:
            word += self.curr
            self.advance()
        if self.curr != "<" and self.curr is not None:
            word += self.curr
        return word.lower()

    def getToken(self, word, tokens, url) -> Token:
        token_return = None
        for t in tokens:
            if isinstance(t.value, TokenWithUri):
                if word == t.value.completeToken(None):
                    token_return = Token(t, t.value.completeToken(url))
                    break
            elif word == t.value or t.value in word:
                token_return = Token(t, t.value)
                break
        return token_return

    def extractURL(self, word, init, end):
        return word.replace(init, "").replace(end, "")

    def getLinesToken(self):
        return self.lines_tokens
