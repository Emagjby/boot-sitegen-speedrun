from htmlnode import HTMLNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return HTMLNode(None, text_node.text, None, None)
        case TextType.BOLD_TEXT:
            return HTMLNode("b", text_node.text, None, None)
        case TextType.ITALIC_TEXT:
            return HTMLNode("i", text_node.text, None, None)
        case TextType.CODE_TEXT:
            return HTMLNode("code", text_node.text, None, None)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("URL must be provided for link text type")

            return HTMLNode("a", text_node.text, None, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("URL must be provided for image text type")

            return HTMLNode(
                "img", None, None, {"src": text_node.url, "alt": text_node.text}
            )
        case _:
            return HTMLNode(None, text_node.text, None, None)
