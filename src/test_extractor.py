import unittest

from extractor import extract_markdown_images, extract_markdown_links


class TestExtractor(unittest.TestCase):
    def test_extract_image(self):
        image = "![Image](https://example.com/image.png) Some text ![Another Image](https://example.com/another-image.png)"
        expected = [
            ("Image", "https://example.com/image.png"),
            ("Another Image", "https://example.com/another-image.png"),
        ]

        extracted = extract_markdown_images(image)
        self.assertEqual(extracted, expected)

    def test_extract_image_no_images(self):
        image = "This is some text without images."
        expected = []

        extracted = extract_markdown_images(image)
        self.assertEqual(extracted, expected)

    def test_extract_image_malformed(self):
        image = "![Image](https://example.com/image.png Some text ![Another Image](https://example.com/another-image.png"
        expected = []

        extracted = extract_markdown_images(image)
        self.assertEqual(extracted, expected)

    def test_extract_image_empty_string(self):
        image = ""
        expected = []

        extracted = extract_markdown_images(image)
        self.assertEqual(extracted, expected)

    def test_extract_link_with_image(self):
        image = "![Image](https://example.com/image.png) [Link](https://example.com)"
        expected = [
            ("Image", "https://example.com/image.png"),
        ]

        extracted = extract_markdown_images(image)
        self.assertEqual(extracted, expected)

    def test_extract_link(self):
        link = "[Link](https://example.com) Some text [Another Link](https://example.com/another)"
        expected = [
            ("Link", "https://example.com"),
            ("Another Link", "https://example.com/another"),
        ]

        extracted = extract_markdown_links(link)
        self.assertEqual(extracted, expected)

    def test_extract_link_no_links(self):
        link = "This is some text without links."
        expected = []

        extracted = extract_markdown_links(link)
        self.assertEqual(extracted, expected)

    def test_extract_link_malformed(self):
        link = "[Link](https://example.com Some text [Another Link](https://example.com/another"
        expected = []

        extracted = extract_markdown_links(link)
        self.assertEqual(extracted, expected)


if __name__ == "__main__":
    _ = unittest.main()
