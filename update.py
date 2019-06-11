import audit

# Create list of mappings to correct abbreviations and other issues to make names consistent.
street_type_mapping = { "S": "South",
                       "Rd": "Road",
                       "Dr": "Drive",
                       "E": "East",
                       "St": "Street", 
                       "W.": "West",
                       "Ave": "Avenue",
                       "Cir": "Circle",
                       "Blvd": "Boulevard",
                       "Ln": "Lane",
                       "W": "West",
                       "Pl": "Place",
                       "s": "South"
                      }

# Define function to correct the issues found in the audit, update per mapping
def fix_street(osmfile):
    st_types = audit.audit_file(osmfile)
    for st_type, ways in st_types.items():
        for name in ways:
            if st_type in street_type_mapping:
                better_name = name.replace(st_type, street_type_mapping[st_type])
                print (name, "=>", better_name)
				
def update_street_name(value):
    m = audit.street_type_re.search(value)
    if m:
        if m.group() in street_type_mapping:
            startpos = value.find(m.group())
            value = value[:startpos] + street_type_mapping[m.group()]
        return value
    else:
        return None
    
                        
def update_value(value, key):
    if key == "addr:street":
        return update_street_name(value)
    else:
        return value
                       
def update_type(key):
    if ":type" in key:
         pass
    elif "_type" in key:
         key = key[:(key.find("_type"))] + ":type"
    elif "type" in key and key.find("type") != 0:
         key = key[:(key.find("type"))] + ":type"
    return key