# Script: 033_parse_xml.py

# Importing the xml.etree.ElementTree module to work with XML data
import xml.etree.ElementTree as ET

# Parsing the XML file 'data.xml' and getting the tree structure
tree = ET.parse('data.xml')

# Getting the root element of the XML tree
root = tree.getroot()

# Iterating through each child element of the root and printing the tag and attributes
for child in root:
    print(child.tag, child.attrib)
