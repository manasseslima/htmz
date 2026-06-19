from __future__ import annotations


class Element:
    def __init__(self, *content: Element | str, tag: str, cls: str | None = None, **attrs):
        self.tag = tag
        self.content = content if content is not None else []
        self.cls = cls
        self.attrs = attrs

    def __str__(self):
        content_str = "".join(str(c) for c in self.content)
        attrs_str = " ".join(f'{k}="{v}"' for k, v in self.attrs.items())
        if self.cls:
            attrs_str += f' class="{self.cls}"'
        return f"<{self.tag} {attrs_str}>{content_str}</{self.tag}>"

    def render(self) -> str:
        return str(self)


class Div(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="div", cls=cls, **attrs)


class Span(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="span", cls=cls, **attrs)


class P(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="p", cls=cls, **attrs)


class H1(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h1", cls=cls, **attrs)

class H2(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h2", cls=cls, **attrs)


class H3(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h3", cls=cls, **attrs)   


class H4(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h4", cls=cls, **attrs)


class H5(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h5", cls=cls, **attrs)   


class H6(Element):
    def __init__(self, *content: Element | str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="h6", cls=cls, **attrs)


class A(Element):
    def __init__(self, *content: Element | str, href: str, cls: str | None = None, **attrs):
        super().__init__(*content, tag="a", cls=cls, href=href, **attrs)
