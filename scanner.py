from tokens import Token, TokenType, TokenWithUri

class Scanner:
    
    def __init__(self, text) -> None:
        self.it = iter(text)
        self.curr = None
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
        
        for t in tokens:
            if(isinstance(t.value, TokenWithUri)):
                tokens_with_uri.append(t)
        
        while self.curr is not None:
            if self.curr in ('\n', '\t', ' '):
                self.advance()
            else:
                if(self.curr == '<'):
                    
                    word = self.getWord()

                    if(tokens_with_uri):
                        for t_uri in tokens_with_uri:
                            if(t_uri.value.init_name in word and word.endswith(t_uri.value.end_name)):
                                return self.getToken(t_uri.value.completeToken(), tokens)

                    if(word in tokens_values):
                        return self.getToken(word, tokens)
                    
                self.advance()
                
        return None
    
    def scanAll(self):
        tokens = []
        while True:
            token = self.scan()
            if token is None:
                break
            tokens.append(token)
        return tokens
                
    def getWord(self) -> str:
        word = ''
        while(self.curr != '>' and self.curr is not None):
            word += self.curr
            self.advance()
        word += self.curr if self.curr != None else ''
        if(self.curr != None):
            self.advance()       
        return word
    
    def getToken(self, word, tokens) -> Token:
        token_return = None
        for t in tokens:
            if(isinstance(t.value, TokenWithUri)):
                if(word == t.value.completeToken()):
                    token_return = Token(t, t.value.completeToken())
                    break
            elif(word == t.value or t.value in word):
                token_return = Token(t, t.value)
                break
        return token_return