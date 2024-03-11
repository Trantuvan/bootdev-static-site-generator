from leafnode import LeafNode
from parentnode import ParentNode

def main():
    node = ParentNode(
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        "p"
    )    
    print(node.to_html())

if __name__ == "__main__":
    main()