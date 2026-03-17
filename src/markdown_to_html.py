from conversion import text_node_to_html_node
from htmlnode import HTMLNode
from splitter import markdown_to_blocks, text_to_textnodes


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = [text_node_to_html_node(node) for node in text_nodes]
    for child in children:
        if child.tag == "b":
            child.tag = "strong"
        elif child.tag == "i":
            child.tag = "em"
    return children


def heading_level(block: str) -> int:
    level = 0
    for char in block:
        if char == "#":
            if level >= 6:
                break
            level += 1
        else:
            break
    return level


def block_to_html_node(block: str) -> HTMLNode:
    match block:
        case block if block.startswith("#"):
            level = heading_level(block)
            text = block[level + 1 :].strip()

            return HTMLNode(
                tag=f"h{level}",
                children=text_to_children(text),
            )
        case block if block.startswith("```"):
            return HTMLNode(
                tag="pre",
                children=[HTMLNode(tag="code", value=block[3:-3].strip())],
            )
        case block if block.startswith(">"):
            return HTMLNode(
                tag="blockquote",
                children=text_to_children(block[1:].strip()),
            )
        case block if block.startswith("- "):
            return HTMLNode(
                tag="ul",
                children=[
                    HTMLNode(
                        tag="li",
                        children=text_to_children(line[2:].strip()),
                    )
                    for line in block.splitlines()
                    if line.startswith("- ")
                ],
            )
        case block if block.startswith(tuple(f"{i}. " for i in range(1, 10))):
            return HTMLNode(
                tag="ol",
                children=[
                    HTMLNode(
                        tag="li",
                        children=text_to_children(line[line.find(". ") + 2 :].strip()),
                    )
                    for line in block.splitlines()
                    if line.startswith(tuple(f"{i}. " for i in range(1, 10)))
                ],
            )
        case _:
            text = " ".join(block.splitlines())
            return HTMLNode(
                tag="p",
                children=text_to_children(text),
            )


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return HTMLNode(tag=None, children=children)
