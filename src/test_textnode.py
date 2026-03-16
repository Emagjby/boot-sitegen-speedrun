import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_bold_text_is_not_same_as_italic(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_text_is_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a different text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_textnode_is_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, "This is a text node")

    def test_has_url_is_not_eq_to_as_no_url(self):
        node = TextNode(
            "This is a text node", TextType.BOLD_TEXT, url="https://example.com"
        )
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    _ = unittest.main()
