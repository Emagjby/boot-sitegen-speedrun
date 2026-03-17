import unittest

from splitter import (
    markdown_to_blocks,
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestSplitter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = [
            TextNode(
                "This is a python example: `print('Hello, World!')`. Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "`"

        expected = [
            TextNode("This is a python example: ", TextType.TEXT),
            TextNode("print('Hello, World!')", TextType.CODE_TEXT),
            TextNode(". Run it!", TextType.TEXT),
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.CODE_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_multiple(self):
        node = [
            TextNode(
                "This is a python example: `print('Hello, World!')`. Run it! `Another code snippet`",
                TextType.TEXT,
            )
        ]

        delimiter = "`"

        expected = [
            TextNode("This is a python example: ", TextType.TEXT),
            TextNode("print('Hello, World!')", TextType.CODE_TEXT),
            TextNode(". Run it! ", TextType.TEXT),
            TextNode("Another code snippet", TextType.CODE_TEXT),
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.CODE_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_multiple_nodes(self):
        node = [
            TextNode("This is a python example: ", TextType.TEXT),
            TextNode("`print('Hello, World!')`", TextType.TEXT),
            TextNode(". Run it! ", TextType.TEXT),
            TextNode("`Another code snippet`", TextType.TEXT),
        ]

        delimiter = "`"

        expected = [
            TextNode("This is a python example: ", TextType.TEXT),
            TextNode("print('Hello, World!')", TextType.CODE_TEXT),
            TextNode(". Run it! ", TextType.TEXT),
            TextNode("Another code snippet", TextType.CODE_TEXT),
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.CODE_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_no_delimiter(self):
        node = [
            TextNode(
                "This is a python example: print('Hello, World!'). Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "`"

        expected = [
            TextNode(
                "This is a python example: print('Hello, World!'). Run it!",
                TextType.TEXT,
            )
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.CODE_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_unmatched_delimiter_errors(self):
        node = [
            TextNode(
                "This is a python example: `print('Hello, World!'). Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "`"

        with self.assertRaises(ValueError):
            split_nodes_delimiter(node, delimiter, TextType.CODE_TEXT)

    def test_split_nodes_delimiter_italic(self):
        node = [
            TextNode(
                "This is an italic example: *italic text*. Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "*"

        expected = [
            TextNode("This is an italic example: ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC_TEXT),
            TextNode(". Run it!", TextType.TEXT),
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.ITALIC_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_bold(self):
        node = [
            TextNode(
                "This is a bold example: **bold text**. Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "**"

        expected = [
            TextNode("This is a bold example: ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(". Run it!", TextType.TEXT),
        ]

        splitted = split_nodes_delimiter(node, delimiter, TextType.BOLD_TEXT)
        self.assertEqual(splitted, expected)

    def test_split_nodes_delimiter_unmatched_bold_delimiter_errors(self):
        node = [
            TextNode(
                "This is a bold example: **bold text. Run it!",
                TextType.TEXT,
            )
        ]

        delimiter = "**"

        with self.assertRaises(ValueError):
            split_nodes_delimiter(node, delimiter, TextType.BOLD_TEXT)

    def test_split_nodes_links(self):
        node = [
            TextNode(
                "This is a link to [Google](https://www.google.com) and [GitHub](https://www.github.com)",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode("This is a link to ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("GitHub", TextType.LINK, "https://www.github.com"),
        ]

        splitted = split_nodes_links(node)
        self.assertEqual(splitted, expected)

    def test_split_nodes_links_no_links(self):
        node = [
            TextNode(
                "This is some text without links.",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode(
                "This is some text without links.",
                TextType.TEXT,
            )
        ]

        splitted = split_nodes_links(node)
        self.assertEqual(splitted, expected)

    def test_split_nodes_links_malformed_link(self):
        node = [
            TextNode(
                "This is a link to [Google](https://www.google.com and [GitHub](https://www.github.com",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode(
                "This is a link to [Google](https://www.google.com and [GitHub](https://www.github.com",
                TextType.TEXT,
            )
        ]

        splitted = split_nodes_links(node)
        self.assertEqual(splitted, expected)

    def test_split_nodes_links_link_with_image_and_split_images(self):
        node = [
            TextNode(
                "This is a link to [Google](https://www.google.com) and ![Image](https://example.com/image.png)",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode("This is a link to ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Image", TextType.IMAGE, "https://example.com/image.png"),
        ]

        splitted = split_nodes_images(node)
        splitted = split_nodes_links(splitted)
        self.assertEqual(splitted, expected)

    def test_split_nodes_images(self):
        node = [
            TextNode(
                "This is an image: ![Image](https://example.com/image.png) and ![Another Image](https://example.com/another-image.png)",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode("This is an image: ", TextType.TEXT),
            TextNode("Image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "Another Image", TextType.IMAGE, "https://example.com/another-image.png"
            ),
        ]

        splitted = split_nodes_images(node)
        self.assertEqual(splitted, expected)

    def test_split_nodes_images_no_images(self):
        node = [
            TextNode(
                "This is some text without images.",
                TextType.TEXT,
            )
        ]

        expected = [
            TextNode(
                "This is some text without images.",
                TextType.TEXT,
            )
        ]

        splitted = split_nodes_images(node)
        self.assertEqual(splitted, expected)

    def test_split_images_two(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **bold** text with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image",
                TextType.IMAGE,
                "https://i.imgur.com/fJRm4Vk.jpeg",
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        textnodes = text_to_textnodes(text)
        self.assertEqual(textnodes, expected)

    def test_text_to_textnodes_no_formatting(self):
        text = "This is some plain text without any formatting."
        expected = [
            TextNode(
                "This is some plain text without any formatting.",
                TextType.TEXT,
            )
        ]

        textnodes = text_to_textnodes(text)
        self.assertEqual(textnodes, expected)

    def test_text_to_textnodes_only_formatting(self):
        text = "**bold** _italic_ `code block` ![image](https://example.com/image.png) [link](https://example.com)"
        expected = [
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" ", TextType.TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]

        textnodes = text_to_textnodes(text)
        self.assertEqual(textnodes, expected)

    def test_text_to_textnodes_unmatched_delimiters(self):
        text = "This is **bold text with unmatched delimiters."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text_to_textnodes_multiple_unmatched_delimiters(self):
        text = "This is **bold text with unmatched *italic delimiters."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_lines(self):
        md = """
This is a paragraph with empty lines before and after.
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["This is a paragraph with empty lines before and after."]
        )

    def test_markdown_to_blocks_only_empty_lines(self):
        md = """


        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    _ = unittest.main()
