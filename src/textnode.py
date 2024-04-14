from htmlnode import LeafNode
class TextNode:
    def __init__(self, text :str, text_type :str, url :str=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode( {self.text}, {self.text_type}, {self.url} )"
    
allowed_types = {
                "text_type_text", 
                 "text_type_bold", 
                 "text_type_italic", 
                 "text_type_code", 
                 "text_type_link", 
                 "text_type_image"
                 }


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Invalid text node - provide node of TextNode class")
    if text_node.text_type not in allowed_types:
        raise ValueError("Invalid text type")
    if text_node.text_type[10:] == "text":
        return LeafNode(value=text_node.text)
    if text_node.text_type[10:] == "bold":
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type[10:] == "italic":
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type[10:] == "code":
        return LeafNode(tag="code", value=text_node.text)
    

    if text_node.text_type[10:] == "link":
        """Provide anchor text and href properties"""

        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    if text_node.text_type[10:] == "image":
        """Provide image source and alt properties
        By default, value set to empty string
        Give image url in src property
        Give image alt text in alt property"""
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    

def split_nodes_delimiter(old_nodes :list[object], delimiter :str, text_type :str) -> list[object]:
    """Takes a list of "old nodes", a delimiter, and a text type. Returns a new list of nodes, where any "text" type nodes in the input list are split into multiple nodes based on the syntax. The delimiter is not included in the output nodes."""
    pass
