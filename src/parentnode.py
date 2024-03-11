from typing import List
from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, children: List[HtmlNode], tag:str=None, props:dict[str, str]|None=None):
        super().__init__(tag, None, children, props=props)
    
    def to_html(self)->str:
        if self.tag is None:
            raise ValueError("You must specify a tag")
        if self.children is None:
            raise ValueError("You must specify at least one child")
        childrenHtml = ""
        for node in self.children:
            childrenHtml += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childrenHtml}</{self.tag}>"