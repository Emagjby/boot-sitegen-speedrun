import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph")
        expected_repr = "LeafNode(p, This is a paragraph, None)"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "my-paragraph"})
        expected_html = '<p class="my-paragraph">This is a paragraph</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        expected_html = "<p>This is a paragraph</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_none_tag(self):
        node = LeafNode(None, "This is just text")
        expected_html = "This is just text"
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    _ = unittest.main()
