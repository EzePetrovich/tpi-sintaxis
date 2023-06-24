from tokens import Token, TokenType, TokenWithUri


class Scanner:
    def __init__(self, text) -> None:
        self.it = iter(text)
        self.curr = None
        self.line = 1
        self.lines_tokens = [dict(tokens=[], line=self.line)]
        self.URL = []
        self.advance()

    def advance(self):
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None

    def scan(self):
        tokens_values = [t.value for t in TokenType]
        tokens = [t for t in TokenType]
        tokens_with_uri = []
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
                                self.URL.append(
                                    word.replace(t_uri.value.init_name, "").replace(
                                        t_uri.value.end_name, ""
                                    )
                                )
                                return self.getToken(
                                    t_uri.value.completeToken(), tokens
                                )
                        else:
                            if word in tokens_values:
                                return self.getToken(word, tokens)
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

    def getToken(self, word, tokens) -> Token:
        token_return = None
        for t in tokens:
            if isinstance(t.value, TokenWithUri):
                if word == t.value.completeToken():
                    token_return = Token(t, t.value.completeToken())
                    break
            elif word == t.value or t.value in word:
                token_return = Token(t, t.value)
                break
        return token_return

    def processURL(self, url):
        pass

    def getLinesToken(self):
        return self.lines_tokens
