# Script: 035_create_and_write_xml.py

# Importing the xml.etree.ElementTree module to work with XML data
import xml.etree.ElementTree as ET

# Creating the root element of the XML tree
root = ET.Element('root')

# Creating child elements 'child1' and 'child2' under the root element
child1 = ET.SubElement(root, 'child1')
child2 = ET.SubElement(root, 'child2')

# Assigning text to the child elements
child1.text = 'Hello'
child2.text = 'World'

# Writing the XML structure to a file 'output.xml' with UTF-8 encoding and XML declaration
tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
