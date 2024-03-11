from leafnode import LeafNode

def main():
    leafNode1 = LeafNode("p", "This is a paragraph of text.")
    leafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
    
    print(leafNode1.to_html())
    print(leafNode2.to_html())

if __name__ == "__main__":
    main()