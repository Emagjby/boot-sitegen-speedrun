from typing import override

from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode | LeafNode],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, None, children, props)

    @override
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    @override
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")

        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")

        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
