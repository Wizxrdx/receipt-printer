class Receipt:
    def __init__(self, paper_width_mm: int = 58) -> None:
        self.__paper_width = paper_width
        self.__contents = []

    def setHeader(self, header: Header = None) -> None:
        self.__header = header
        
    def setBody(self, body: Body = None) -> None:
        self.__body = body

    def setFooter(self, footer: Footer = None) -> None:
        self.__footer = footer

    def print(self) -> bool:
        if self.__body is None:
            return()

    def addContent(self, content: dict = {}) -> None:
        # TODO: check content
        self.__contents.append(content)

    def setContent(self, contents: list = []) -> None:
        # TODO: check content
        self.__contents = contents

    def getContent(self) -> list:
        return self.__contents

    def addLine(self, text: str = "", size: int = 200, italic: bool = False, underline: bool = False, ) -> None:
        
