import unittest

from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode("a", "https://www.boot.dev", props={'href': "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_repr(self):
        node = HtmlNode("a", "https://www.boot.dev", props={'href': "https://www.boot.dev"})
        self.assertEqual(repr(node), 'HtmlNode(a, https://www.boot.dev, None, {\'href\': \'https://www.boot.dev\'})')
        
    def test_to_html_many_children(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "h2",
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()