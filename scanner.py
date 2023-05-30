from tokens import Token, TokenType

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
        tokens_values = [t.value for t in TokenType];
        while self.curr is not None:
            if self.curr in ('\n', '\t', ' '):
                self.advance()
            else:
                word = self.getWord()
                
                if(word == '<article>'):
                    return Token(TokenType.ARTICLE_O, '<article>')
                elif(word == '</article>'):
                    return Token(TokenType.ARTICLE_C, '</article>')

                if(word in tokens_values):
                    print("Es token")
                else:
                    print("No es token")
                self.advance()
                
                #raise Exception('Caracter no reconocido.')
                #raise Exception('Token no reconocido.')
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
        word += self.curr;
        return word
'''

elif self.curr == 't':
    self.verify('true')
    return Token(TokenType.TRUE, 'true')
elif self.curr == 'f':
    self.verify('false')
    return Token(TokenType.FALSE, 'false')
elif self.curr == 'a':
    self.verify('and')
    return Token(TokenType.AND, 'and')
 elif self.curr == 'o':
    self.verify('or')
    return Token(TokenType.OR, 'or')
elif self.curr == 'n':
    self.verify('not')
    return Token(TokenType.NOT, 'not')

'''