

class Element:
    def __init__(self, tag: str, content: Element = ""):
        self.tag = tag
        self.content = content

    def __str__(self):
        return f"<{self.tag}>{self.content}</{self.tag}>"
