class HTMLNode:
    def __init__(self, 
                 tag :str = None, 
                 value :str = None, 
                 children :list[object] = [],
                 props :dict[str, str] = {}
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            props_html = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
            return ' ' + props_html
        return ""
    
    def __repr__(self):
        return (
            f"<HTMLNode(tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props})>"
        )

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props={}):
        super().__init__(tag=tag, value=value, props=props, children=[])
        
    def to_html(self) -> str:
        """Renders leaf node as HTMl string"""
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list[object] = [], props: dict[str, str] = {}):
        if not children:
            raise ValueError("Parent Node must have children")
        if not tag:
            raise ValueError("Tag not provided")
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        pass