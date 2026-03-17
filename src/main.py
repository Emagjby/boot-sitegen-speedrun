from extractor import extract_markdown_images
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from splitter import (
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)
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

splitter_1_node = TextNode("This is text with a `code block` word", TextType.TEXT)
splitter_1_new_nodes = split_nodes_delimiter([splitter_1_node], "`", TextType.CODE_TEXT)

splitter_2_node = TextNode(
    "This is a link to [Google](https://www.google.com) and [GitHub](https://www.github.com)",
    TextType.TEXT,
)
splitter_2_new_nodes = split_nodes_images([splitter_2_node])

splitter_3_node = TextNode(
    "This is a link to [Google](https://www.google.com) and ![Image](https://example.com/image.png)",
    TextType.TEXT,
)
splitter_3_new_nodes = split_nodes_images([splitter_3_node])
splitter_3_new_nodes = split_nodes_links([*splitter_3_new_nodes])

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
formatted = text_to_textnodes(text)

print(node)
print(node2)
print(html_node)
print(html_node_2)
print(leaf_node)
print(parent_node)
print(parent_node.to_html())

print("---------------------\n\n")

print(splitter_1_new_nodes)
print(splitter_2_new_nodes)
print(splitter_3_new_nodes)

print("---------------------\n\n")

print(
    extract_markdown_images(
        "![Image](https://example.com/image.png) Some text ![Another Image](https://example.com/another-image.png)"
    )
)

print("---------------------\n\n")

print(text)
print(formatted)
