# Caleb Potts
# 03/03/2024

# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.
from pprint import pprint

for item in data:
    if "tag1" in item["tags"]:
        item["tags"].append("tag4")

pprint(data)
