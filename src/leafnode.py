from typing import override

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        props_str = self.props_to_html()
        if self.tag is None:
            return f"{self.value}"

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    @override
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
