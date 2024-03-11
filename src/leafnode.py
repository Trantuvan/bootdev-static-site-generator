from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag:str=None,value:str=None, props:dict[str, str]|None=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value must be specified")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        