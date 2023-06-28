class TokenWithUri:
    def __init__(self, init_name, end_name):
        self.init_name = init_name
        self.end_name = end_name if end_name else '"/>'

    def completeToken(self, url):
        return self.init_name + self.end_name + url if url != None else ""
