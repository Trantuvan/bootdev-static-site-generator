class TextNode:
    def __init__(self, text:str, text_type:str, url:str=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: "TextNode") -> bool:
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"