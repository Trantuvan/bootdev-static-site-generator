import unittest
from typing import Tuple

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode("a", "https://www.boot.dev", props={'href': "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_repr(self):
        node = HtmlNode("a", "https://www.boot.dev", props={'href': "https://www.boot.dev"})
        self.assertEqual(repr(node), 'HtmlNode(a, https://www.boot.dev, None, {\'href\': \'https://www.boot.dev\'})')

if __name__ == "__main__":
    unittest.main()