import unittest

from conversion import text_node_to_html_node
from textnode import TextNode, TextType


class TestConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is bold text", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic_text(self):
        node = TextNode("This is italic text", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code_text(self):
        node = TextNode("This is code text", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode(
            "This is an image", TextType.IMAGE, url="https://example.com/image.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/image.png", "alt": "This is an image"},
        )

    def test_link_without_url(self):
        node = TextNode("This is a link without URL", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_without_url(self):
        node = TextNode("This is an image without URL", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    _ = unittest.main()
