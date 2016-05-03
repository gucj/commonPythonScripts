# coding=utf-8
__author__ = 'gucuijuan'

"parse xml"

from xml.dom import minidom
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_nodes_by_tag_name(node, tag_name):
    """
     get node from parent node by tagName
     :param node:node
     :param tag_name:tagName
     :return:elements
    """
    return node.getElementsByTagName(tag_name) if node else []


def get_node_value(node):
    return node.firstChild.data if node else ""


def get_attr_value(node, attr_name):
    """
    get attribute value from node
    :param node:
    :param attr_name:
    :return:
    """
    return node.getAttribute(attr_name) if node else ""


def get_xml_data(filename):
    """
    get xml data
    :param filename:
    :return:
    """
    doc = minidom.parse(filename)
    root = doc.documentElement
    return root


def get_node_when_attr_equal(nodes, attr_name, attr_value):
    result_node = None

    for node in nodes:
        value = get_attr_value(node, attr_name)
        if unicode(value) == unicode(attr_value):
            result_node = node
    return result_node

