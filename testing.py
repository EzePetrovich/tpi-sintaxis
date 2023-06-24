class TokenWithUri:
    def __init__(self, init_name, end_name):
        self.init_name = init_name
        self.end_name = end_name if end_name else '"/>'

    def completeToken(self):
        return self.init_name + self.end_name


protocols = ["http", "https", "ftp", "ftps"]
