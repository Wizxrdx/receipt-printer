class Content:
    def __init__(self, contents: list = []):
        self.__contents = []

    def addContent(self, content: dict = {}) -> None:
        # TODO: check content
        self.__contents.append(content)

    def setContent(self, contents: list = []) -> None:
        # TODO: check content
        self.__contents = contents

    def getContent(self) -> list:
        return self.__contents

    def addLine(self, text: str = "", size: int = 200, italic: bool = False, underline: bool = False, ) -> None:
        
