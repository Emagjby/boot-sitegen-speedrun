import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_repr_with_simple_parents(self):
        parent_node = ParentNode("div", [], {"class": "parent"})
        expected_repr = "ParentNode(div, [], {'class': 'parent'})"
        self.assertEqual(repr(parent_node), expected_repr)

    def test_repr_with_props(self):
        parent_node = ParentNode("div", [], {"class": "parent", "id": "main"})
        expected_repr = "ParentNode(div, [], {'class': 'parent', 'id': 'main'})"
        self.assertEqual(repr(parent_node), expected_repr)

    def test_repr_with_nested_children(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        parent_node = ParentNode("div", [child_node1, child_node2], {"class": "parent"})
        expected_repr = "ParentNode(div, [LeafNode(span, Child Node 1, None), LeafNode(span, Child Node 2, None)], {'class': 'parent'})"
        self.assertEqual(repr(parent_node), expected_repr)

    def test_one_parent_with_one_leaf_child(self):
        child_node = LeafNode("span", "Child Node")
        parent_node = ParentNode("div", [child_node], {"class": "parent"})
        expected_html = '<div class="parent"><span>Child Node</span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_one_parent_with_multiple_leaf_children(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        parent_node = ParentNode("div", [child_node1, child_node2], {"class": "parent"})
        expected_html = '<div class="parent"><span>Child Node 1</span><span>Child Node 2</span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_one_parent_with_props_and_multiple_children(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        parent_node = ParentNode(
            "div", [child_node1, child_node2], {"class": "parent", "id": "main"}
        )
        expected_html = '<div class="parent" id="main"><span>Child Node 1</span><span>Child Node 2</span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_one_parent_with_props_and_multiple_children(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        parent_node = ParentNode(
            "div", [child_node1, child_node2], {"class": "parent", "id": "main"}
        )
        expected_html = '<div class="parent" id="main"><span>Child Node 1</span><span>Child Node 2</span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_parent_containing_another_parent(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        inner_parent_node = ParentNode("div", [child_node1], {"class": "inner"})
        outer_parent_node = ParentNode(
            "div", [inner_parent_node, child_node2], {"class": "outer"}
        )
        expected_html = '<div class="outer"><div class="inner"><span>Child Node 1</span></div><span>Child Node 2</span></div>'
        self.assertEqual(outer_parent_node.to_html(), expected_html)

    def test_parent_containing_multiple_parents(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        inner_parent_node1 = ParentNode("div", [child_node1], {"class": "inner1"})
        inner_parent_node2 = ParentNode("div", [child_node2], {"class": "inner2"})
        outer_parent_node = ParentNode(
            "div", [inner_parent_node1, inner_parent_node2], {"class": "outer"}
        )
        expected_html = '<div class="outer"><div class="inner1"><span>Child Node 1</span></div><div class="inner2"><span>Child Node 2</span></div></div>'
        self.assertEqual(outer_parent_node.to_html(), expected_html)

    def parent_containing_mix_of_leafnode_and_parentnode(self):
        child_node1 = LeafNode("span", "Child Node 1")
        child_node2 = LeafNode("span", "Child Node 2")
        inner_parent_node = ParentNode("div", [child_node1], {"class": "inner"})
        outer_parent_node = ParentNode(
            "div", [inner_parent_node, child_node2], {"class": "outer"}
        )
        expected_html = '<div class="outer"><div class="inner"><span>Child Node 1</span></div><span>Child Node 2</span></div>'
        self.assertEqual(outer_parent_node.to_html(), expected_html)

    def test_tag_none_should_raise_value_error(self):
        child_node = LeafNode("span", "Child Node")
        parent_node = ParentNode(None, [child_node], {"class": "parent"})
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_children_none_should_raise_value_error(self):
        parent_node = ParentNode("div", None, {"class": "parent"})
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def empty_children_list_should_return_opening_and_closing_tags(self):
        parent_node = ParentNode("div", [], {"class": "parent"})
        expected_html = '<div class="parent"></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_props_is_none(self):
        child_node = LeafNode("span", "Child Node")
        parent_node = ParentNode("div", [child_node], None)
        expected_html = "<div><span>Child Node</span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_props_is_empty_dict(self):
        child_node = LeafNode("span", "Child Node")
        parent_node = ParentNode("div", [child_node], {})
        expected_html = "<div><span>Child Node</span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def props_with_multiple_attributes(self):
        child_node = LeafNode("span", "Child Node")
        parent_node = ParentNode(
            "div", [child_node], {"class": "parent", "id": "main", "data-test": "value"}
        )
        expected_html = '<div class="parent" id="main" data-test="value"><span>Child Node</span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)


if __name__ == "__main__":
    _ = unittest.main()
