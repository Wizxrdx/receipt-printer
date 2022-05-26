class Receipt:
    def __init__(self, paper_width_mm: int = 58) -> None:
        self.__paper_width = paper_width
        self.__header = None
        self.__body = None
        self.__footer = None

    def setHeader(self, header: Header = None) -> None:
        self.__header = header
        
    def setBody()self, body: Body = None) -> None:
        self.__body = body

    def setFooter()self, footer: Footer = None) -> None:
        self.__footer = footer

    def print(self) -> bool:
        if self.__body is None:
            return()
