class Header(content):
    def __init__(self, contents: list = []):
        super().__init__(contents)
        self.__name = 'header'

    def getName(self):
        return self.__name
