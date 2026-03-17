import unittest

from markdown_to_html import extract_title, markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bold** text
text is a p
tag here

This is another paragraph with *italic* text and `code`.

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <strong>bold</strong> text text is a p tag here</p><p>This is another paragraph with <em>italic</em> text and <code>code</code>.</p></div>",
        )

    def test_headings(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1></div>",
        )

        md = "## Heading 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading 2</h2></div>",
        )

        md = "### Heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading 3</h3></div>",
        )

    def test_blockquotes(self):
        md = "> This is a blockquote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote</blockquote></div>",
        )

    def test_code_blocks(self):
        md = """```
def hello():
    print("Hello, World!")
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def hello():\n    print(&quot;Hello, World!&quot;)</code></pre></div>",
        )

    def test_lists(self):
        md = """- Item 1
- Item 2
- Item 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

        md = """1. First
2. Second
3. Third"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>",
        )

    def test_extract_title(self):
        md = "# My Title"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_with_spaces(self):
        md = "#    My Title     "
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_raises_with_no_title(self):
        md = "This is not a title"
        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    _ = unittest.main()
