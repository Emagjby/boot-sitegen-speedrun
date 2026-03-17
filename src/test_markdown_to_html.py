import unittest

from markdown_to_html import markdown_to_html_node


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
            "<p>This is <strong>bold</strong> text text is a p tag here</p><p>This is another paragraph with <em>italic</em> text and <code>code</code>.</p>",
        )

    def test_headings(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<h1>Heading 1</h1>",
        )

        md = "## Heading 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<h2>Heading 2</h2>",
        )

        md = "### Heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<h3>Heading 3</h3>",
        )

    def test_blockquotes(self):
        md = "> This is a blockquote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<blockquote>This is a blockquote</blockquote>",
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
            "<pre><code>def hello():\n    print(&quot;Hello, World!&quot;)</code></pre>",
        )

    def test_lists(self):
        md = """- Item 1
- Item 2
- Item 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>",
        )

        md = """1. First
2. Second
3. Third"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<ol><li>First</li><li>Second</li><li>Third</li></ol>",
        )


if __name__ == "__main__":
    _ = unittest.main()
