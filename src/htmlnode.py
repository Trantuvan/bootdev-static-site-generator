from typing import List, Dict

class HtmlNode:
    def __init__(self, tag:str=None, value:str=None, children: List["HtmlNode"]=None, props:Dict[str, str]=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self)->str:
        result = ""
        
        if self.props is None:
            return result
        
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        
        return result

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"