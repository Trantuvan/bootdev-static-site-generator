import unittest
from ddt import ddt, data, unpack
from typing import Tuple

from textnode import TextNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

@ddt
class TestTextNode(unittest.TestCase):

    @data((("this is a test text node", "bold"), ("this is a test text node", "bold")),
          (("aa", "italic", "www.google.com"), ("aa", "italic", "www.google.com")))
    @unpack
    def test_eq_true(self, arg1:Tuple[str, str, str|None], arg2:Tuple[str, str, str|None]):
        text1, text_type1, *url1 = arg1
        text2, text_type2, *url2 = arg2

        # *url1, *url2 are meant to be post unpack processed
        url1 = url1[0] if url1 else None
        url2 = url2[0] if url2 else None

        self.assertEqual(TextNode(text1, text_type1, url1), TextNode(text2, text_type2, url2), "Equality tests")
    
    @data((("", "bold"), ("this is a test text node", "bold")),
          (("aa", "italic", "www.google.com"), ("aab", "", "www.google.com")))
    @unpack
    def test_eq_false(self, arg1:Tuple[str, str, str|None], arg2:Tuple[str, str, str|None]):
        text1, text_type1, *url1 = arg1
        text2, text_type2, *url2 = arg2

        # *url1, *url2 are meant to be post unpack processed
        url1 = url1[0] if url1 else None
        url2 = url2[0] if url2 else None

        self.assertNotEqual(TextNode(text1, text_type1, url1), TextNode(text2, text_type2, url2), "Equality tests")

    @data(("this is a test text node", "bold"), 
          ("aa", "italic", "www.google.com"))
    @unpack
    def test_repr_true(self, text:str, text_type:str, url:str=None):
        test = TextNode(text, text_type, url)
        self.assertEqual(repr(test), f"TextNode({text}, {text_type}, {url})", "Representation tests")

    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()

