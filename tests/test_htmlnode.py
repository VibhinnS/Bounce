import sys
import unittest
from unittest.mock import MagicMock
sys.path.append("src")
from htmlnode import HTMLNode, LeafNode, ParentNode
# from nodes.testing_nodes import nodes

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
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {})

        props = {"id": "example", "class": "content"}
        node = LeafNode(value="Hello", tag="p", props=props)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, props)

    def test_to_html(self):
        node = LeafNode(value="Hello", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

        props = {"id": "example", "class": "content"}
        node = LeafNode(value="Hello", tag="p", props=props)
        self.assertEqual(node.to_html(), '<p id="example" class="content">Hello</p>')


class TestParentNodeToHtml(unittest.TestCase):

    def test_to_html_raise_value_error_tag_none(self):
        node = ParentNode(None, [MagicMock()])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raise_value_error_children_none(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_one_child(self):
        child = MagicMock()
        child.to_html.return_value = "<p>Child</p>"

        node = ParentNode("div", [child])
        expected_output = "<div><p>Child</p></div>"

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_multiple_children(self):
        child1 = MagicMock()
        child1.to_html.return_value = "<p>Child1</p>"
        child2 = MagicMock()
        child2.to_html.return_value = "<p>Child2</p>"

        node = ParentNode("div", [child1, child2])
        expected_output = "<div><p>Child1</p><p>Child2</p></div>"

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_one_prop(self):
        child = MagicMock()
        child.to_html.return_value = "<p>Child</p>"

        node = ParentNode("div", [child], {"class": "my-class"})
        expected_output = "<div class=\"my-class\"><p>Child</p></div>"

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_multiple_props(self):
        child = MagicMock()
        child.to_html.return_value = "<p>Child</p>"

        node = ParentNode("div", [child], {"class": "my-class", "id": "my-id"})
        expected_output = "<div class=\"my-class\" id=\"my-id\"><p>Child</p></div>"

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_no_props(self):
        child = MagicMock()
        child.to_html.return_value = "<p>Child</p>"

        node = ParentNode("div", [child])
        expected_output = "<div><p>Child</p></div>"

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
