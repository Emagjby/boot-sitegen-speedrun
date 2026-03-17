from extractor import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Delimiter {delimiter} is not closed in node {node}")

        for j, part in enumerate(parts):
            if part == "":
                continue

            if j % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links: list[str] = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        last_index = 0
        for link in links:
            link_text, link_url = link
            link_index = node.text.find(f"[{link_text}]({link_url})", last_index)

            if link_index == -1:
                continue

            if link_index > last_index:
                new_nodes.append(
                    TextNode(node.text[last_index:link_index], TextType.TEXT)
                )

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            last_index = link_index + len(f"[{link_text}]({link_url})")

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images: list[str] = extract_markdown_links(node.text)

        if not images:
            new_nodes.append(node)
            continue

        last_index = 0
        for image in images:
            image_text, image_url = image
            image_index = node.text.find(f"![{image_text}]({image_url})", last_index)

            if image_index == -1:
                continue

            if image_index > last_index:
                new_nodes.append(
                    TextNode(node.text[last_index:image_index], TextType.TEXT)
                )

            new_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))

            last_index = image_index + len(f"![{image_text}]({image_url})")

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    # Split by delimiters

    delimiters = {
        "**": TextType.BOLD_TEXT,
        "_": TextType.ITALIC_TEXT,
        "`": TextType.CODE_TEXT,
        "*": TextType.ITALIC_TEXT,
    }

    nodes: list[TextNode] = [TextNode(text, TextType.TEXT)]

    for delimiter, text_type in delimiters.items():
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)

    # Split by images

    for node in nodes:
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_images(nodes)
            break

    # Split by links

    for node in nodes:
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_links(nodes)
            break

    return nodes


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks
