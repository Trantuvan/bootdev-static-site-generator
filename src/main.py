from htmlnode import HtmlNode

def main():
    print(HtmlNode("a","https://www.boot.dev", props={'href':"https://www.boot.dev", "target":"_blank"}).props_to_html())

if __name__ == "__main__":
    main()