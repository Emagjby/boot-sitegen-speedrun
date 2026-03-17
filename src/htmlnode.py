from typing import override


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list["HTMLNode"] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> str:
        if self.tag is None:
            if self.children is not None:
                return "".join(child.to_html() for child in self.children)
            if self.value is None:
                raise ValueError("Value cannot be None when tag is None")
            return self.value

        if self.children is not None:
            children_html = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        value = self.value if self.value is not None else ""
        value = (
            value.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )
        return f"<{self.tag}{self.props_to_html()}>{value}</{self.tag}>"

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'

        return props_str

    @override
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
