ssn_name_pairs = dict()

ssn_name_pairs = {}

ssn_name_pairs["123-456-789"] = "John Appleseed"
ssn_name_pairs["000-000-002"] = "Dwight Schrute"
ssn_name_pairs["999-000-005"] = "Pam Beesly"

ssn_name_pairs = {"123-456-789": "John Appleseed", 
                  "000-000-002": "Dwight Schrute",
                  "999-000-005": "Pam Beesly"}

print(ssn_name_pairs)

print(ssn_name_pairs["999-000-005"])

# name = ssn_name_pairs["999-999-999"] # triggers KeyError as the key doesn't exist

ssn_name_pairs["999-000-005"] = "Angela Martin"
print(ssn_name_pairs)

ssn_name_pairs["000-000-006"] = "Andy Bernard"
print(ssn_name_pairs)

key = "000-000-003"
if key in ssn_name_pairs:
    del ssn_name_pairs["000-000-003"]
else:
    print(f"Invalid key {key}")

print(ssn_name_pairs)