class Footer(content):
    def __init__(self, contents: list = []):
        super().__init__(contents)
        self.__name = 'footer'

    def getName(self):
        return self.__name
