import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected_street_types = ["Street", "Avenue", "Drive", "North", "South", "East", "West", "Circle", 
        "Boulevard","Road", "Way", "Court", "Lane", "Place", "Terrace", "Cove", "Row"]

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected_street_types:
            street_types[street_type].add(street_name)
			
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit_file(osmfile):
    osm_file = open(osmfile, "rb")
    street_types = defaultdict(set)
    post_codes = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types