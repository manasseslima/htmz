from .elements import Element


class Html:
    def __init__(
            self, 
            *content: Element | str,
            metas: dict[str, str] | None = None,
            title: str | None = None,
            styles: dict[str, str] | None = None,
            scripts: dict[str, str] | None = None,
        ):
        self.content = content if content is not None else []
        self.metas = metas if metas is not None else {}
        self.title = title if title is not None else ""
        self.styles = styles if styles is not None else {}
        self.scripts = scripts if scripts is not None else {}

    def __str__(self):
        content_str = "".join(str(c) for c in self.content)
        return f"<html><head>{self._render_head()}</head><body>{content_str}</body></html>"

    def render(self) -> str:
        return str(self)
    
    def _render_head(self) -> str:
        metas_str = "".join(f'<meta name="{k}" content="{v}">' for k, v in self.metas.items())
        styles_str = "".join(f'<style>{v}</style>' for v in self.styles.values())
        return f"{metas_str}<title>{self.title}</title>{styles_str}"