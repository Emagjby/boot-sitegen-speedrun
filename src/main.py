from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType

node = TextNode("Hello, World!", TextType.BOLD_TEXT)
node2 = TextNode("Hello, World!", TextType.BOLD_TEXT, "https://example.com")
html_node = HTMLNode("div", None, None, {"class": "my-div"})
html_node_2 = HTMLNode("div", None, [html_node], {"class": "my-div"})
leaf_node = LeafNode("span", "This is a leaf node", {"class": "leaf-node"})
parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node)
print(node2)
print(html_node)
print(html_node_2)
print(leaf_node)
print(parent_node)
print(parent_node.to_html())
