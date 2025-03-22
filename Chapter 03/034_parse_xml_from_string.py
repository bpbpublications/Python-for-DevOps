# Script: 034_parse_xml_from_string.py

# Importing the xml.etree.ElementTree module to work with XML data
import xml.etree.ElementTree as ET

# XML data as a string
xml_data = '<data><item>Hello</item><item>World</item></data>'

# Parsing the XML string into an element tree
root = ET.fromstring(xml_data)

# Iterating through each 'item' element and printing its text content
for item in root.findall('item'):
    print(item.text)
