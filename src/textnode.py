from leafnode import LeafNode
from typing import List

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

delimiter_bold = "**"
delimiter_italic = "*"
delimiter_code = "`"

class TextNode:
    def __init__(self, text:str, text_type:str, url:str=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: "TextNode") -> bool:
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node:type["TextNode"])->str:
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text).to_html()
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text).to_html()
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text).to_html()
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text).to_html()
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href":"www.google.com"}).to_html()
    if text_node.text_type == text_type_image:
        return LeafNode("img", text_node.text, {"src":"www.google.com", "alt":"google imgs"}).to_html()

    raise Exception("cannot convert to html text of type:", text_node.text_type)

def split_nodes_delimiter(old_nodes:List[TextNode], delimiter:str, text_type:str)-> List[TextNode]:
    new_nodes = []
    valid_text_types = [text_type_text,
                        text_type_bold,
                        text_type_italic,
                        text_type_code,
                        text_type_link,
                        text_type_image]

    for node in old_nodes:
        if isinstance(node, TextNode) == False:
            new_nodes.append(node)
        if node.text_type not in valid_text_types:
            continue
        str_array = node.text.split(delimiter)

        if str_array.__len__() % 2 == 0:
            raise Exception("that's invalid Markdown syntax.")

        for i in range(len(str_array)):
            textNode = None
            if i % 2 == 0:
                textNode = TextNode(str_array[i], text_type_text)
            else:
                textNode = TextNode(str_array[i], text_type)
            new_nodes.append(textNode)

    return new_nodes

