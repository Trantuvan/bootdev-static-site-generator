from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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