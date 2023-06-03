from tokens import Token, TokenType, TokenWithUri

class Scanner:
    
    def __init__(self, text) -> None:
        self.it = iter(text)
        self.curr = None
        self.line_num = 1
        self.lines_tokens = []
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
        
        dictionary = {
            'line': self.line_num,
            'tokens': []
        }
        
        self.lines_tokens.append(dictionary)

        while self.curr is not None:
            if self.curr in ('\n', '\t', ' '):
                if self.curr == '\n':
                    self.line_num += 1
                    self.lines_tokens.append(dictionary)
                self.advance()
            else:
                if(self.curr == '<'):
                    word = self.getWord()
                    if(tokens_with_uri):
                        for t_uri in tokens_with_uri:
                            if(t_uri.value.init_name in word and word.endswith(t_uri.value.end_name)):
                                return self.getToken(t_uri.value.completeToken(), tokens)
                    if(word in tokens_values):
                        # Si contiene el caracter '/' es un token de cierre, por lo tanto no tiene más contenido, si var 'content' es vacia no hay token <text>
                        token = self.getToken(word, tokens)
                        #self.lines_tokens[0].tokens.append(token)
                        return token
                else:
                    # Analizar si es texto
                    pass
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
        return word.lower()
    
    def processContent(self):
        pass
    
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


'''
input('--------------------')
        for tokens_dictionary in self.lines_tokens:
            line = 1
            print(f'En la linea {line} se encontraron: ')
            for toks in tokens_dictionary.tokens:
                print(f'{toks}')
            line += 1
        input('----------------------')

'''