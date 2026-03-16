import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node: HTMLNode = HTMLNode("div", "Hello World", None, {"class": "my-div"})
        expected_repr = "HTMLNode(div, Hello World, None, {'class': 'my-div'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node: HTMLNode = HTMLNode("div", "Hello World", None, {"class": "my-div"})
        expected_props_html = ' class="my-div"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_children_to_html(self):
        child_node: HTMLNode = HTMLNode("span", "Child Node", None, {"class": "child"})
        _parent_node: HTMLNode = HTMLNode(
            "div", None, [child_node], {"class": "parent"}
        )
        expected_child_html = ' class="child"'
        self.assertEqual(child_node.props_to_html(), expected_child_html)

    def test_children_repr(self):
        child_node: HTMLNode = HTMLNode("span", "Child Node", None, {"class": "child"})
        parent_node: HTMLNode = HTMLNode("div", None, [child_node], {"class": "parent"})
        expected_repr = "HTMLNode(div, None, [HTMLNode(span, Child Node, None, {'class': 'child'})], {'class': 'parent'})"
        self.assertEqual(repr(parent_node), expected_repr)


if __name__ == "__main__":
    _ = unittest.main()
