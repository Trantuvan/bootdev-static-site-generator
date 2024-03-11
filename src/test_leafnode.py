import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_no_value(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()