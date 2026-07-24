data = {
    "Syntax": ["[]", "()", "{}", "frozenset()", "{}"],
    "Ordered": ["Yes", "Yes", "No", "No", "Yes"],
    "Mutable": ["Yes", "No", "Yes", "No", "Yes"],
    "Allow Duplicates": ["Yes", "Yes", "No", "No", "Keys: No, Values: Yes"],
    "Indexed": ["Yes", "Yes", "No", "No", "Keys"],
    "Heterogeneous": ["Yes", "Yes", "Yes", "Yes", "Yes"],
    "Hashable": ["No", "Yes", "No", "Yes", "No"],
    "Can be Dictionary Key": ["No", "Yes", "No", "Yes", "No"],
    "Can be Nested": ["Yes", "Yes", "Yes", "Yes", "Yes"],
    "Supports Slicing": ["Yes", "Yes", "No", "No", "No"],
    "Lookup Speed": ["O(n)", "O(n)", "O(1)", "O(1)", "O(1)"],
    "Stores": ["Values", "Values", "Unique Values", "Unique Values", "Key-Value Pairs"],
    "Typical Use": ["General Collection", "Fixed Data", "Unique Elements", "Immutable Set", "Mapping Data"]
}

print(f"{'Property':<25}{'List':<20}{'Tuple':<20}{'Set':<20}{'Frozenset':<20}{'Dictionary'}")

for key, value in data.items():
    print(f"{key:<25}{value[0]:<20}{value[1]:<20}{value[2]:<20}{value[3]:<20}{value[4]}")