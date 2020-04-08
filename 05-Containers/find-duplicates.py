ssn_name_pairs = {"123-456-789": "John Appleseed", 
                  "000-000-002": "Dwight Schrute",
                  "999-000-005": "Pam Beesly",
                  "888-888-888": "John Appleseed",
                  "999-000-006": "Pam Beesly",
                  "999-000-007": "Pam Beesly"}


# Expected output
# {"John Appleseed": ['123-456-789', '888-888-888'],
# "Pam Beesly": ['999-000-005', '999-000-006', '999-000-007']}
# if a name appears more than once, create a dictionary with the name as the key and list the SSNs of the duplicate names

def find_duplicate_names(ssn_name_dictionary: dict) -> dict:
    result = {}
    names = list(ssn_name_dictionary.values())    
    for (ssn, name) in ssn_name_dictionary.items():    
        if names.count(name) > 1:
            result[name] = result.get(name, [])
            result[name].append(ssn)
    return result

duplicate_name_ssns = find_duplicate_names(ssn_name_pairs)

for (name, ssns) in duplicate_name_ssns.items():
    print(f"Found duplicate name {name} with SSNs: {ssns}")
