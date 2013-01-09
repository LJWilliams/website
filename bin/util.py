"""
Utilities used in Software Carpentry tools.
"""

import sys
from lxml import etree as ET

#-------------------------------------------------------------------------------

def read_xml(filename, mangle_entities=False):
    """
    Read in a document, returning the ElementTree doc node.
    """
    parser = ET.HTMLParser(recover=False)
    with open(filename, 'r') as reader:
        try:
            return ET.parse(reader, parser)
        except ET.XMLSyntaxError as e:
            print >> sys.stderr, filename, str(e)
            sys.exit(1)

#-------------------------------------------------------------------------------

def write_xml(filename, doc, unmangle_entities=False):
    """
    Write out a document.
    """
    with open(filename, 'w') as writer:
        writer.write(ET.tostring(doc.getroot()))

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    if len(sys.argv) not in (2, 3):
        print >> sys.stderr, 'usage: util.py infile [outfile]'
    doc = read_xml(sys.argv[1])
    if len(sys.argv) == 3:
        write_xml(sys.argv[2], doc)
