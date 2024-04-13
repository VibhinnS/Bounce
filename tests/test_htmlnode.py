import sys
import unittest

sys.path.append("src")
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_node_creation(self):
        node1 = HTMLNode(tag="div", value="Hello")
        self.assertEqual(node1.tag, "div")
        self.assertEqual(node1.value, "Hello")
        self.assertEqual(node1.children, [])
        self.assertEqual(node1.props, {})

        props = {"id": "example", "class": "content"}
        node2 = HTMLNode(tag="p", props=props)
        self.assertEqual(node2.tag, "p")
        self.assertIsNone(node2.value)
        self.assertEqual(node2.children, [])
        self.assertEqual(node2.props, props)

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Title", props={"id": "title"})
        self.assertEqual(repr(node), '<HTMLNode(tag=h1, value=Title, children=[], props={\'id\': \'title\'})>')


class TestLeafNode(unittest.TestCase):
    """Unit tests for LeafNode class"""

    def test_node_creation(self):
        node = LeafNode(value="Hello", tag="p")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

        props = {"id": "example", "class": "content"}
        node = LeafNode(value="Hello", tag="p", props=props)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, props)

    def test_to_html(self):
        node = LeafNode(value="Hello", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

        props = {"id": "example", "class": "content"}
        node = LeafNode(value="Hello", tag="p", props=props)
        self.assertEqual(node.to_html(), '<p id="example" class="content">Hello</p>')


class TestParentNode(unittest.TestCase):
    def test_node_creation(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", props={"id": "example"})
        with self.assertRaises(ValueError):
            ParentNode(children=[LeafNode("Hello", "p")])
        with self.assertRaises(ValueError):
            ParentNode(props={"id": "example"}, children=[LeafNode("Hello", "p")])


if __name__ == "__main__":
    unittest.main()
