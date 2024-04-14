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
    """Creates a leaf node
    
    Args: 
        tag (str): tag name [default None]
        value (str): value of the tag [default None]
        props (dict): tag properties [default {}]
    """
    def __init__(self, tag :str, value :str, props={str:str}):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"    

         