import re
#Regex -> Regular Expression
#Pattern match in a string

# numbers = """
# 38795475, 4985048584, 098305
# """

# #They have 16 digits
# #Start with 4

# quote = "To be or not to be"

# #r - raw
# is_be = re.search(r"be$", quote)
# print(is_be,type(is_be))

# output = "Present" if is_be else "Not present"
# print(output)

# quote1 = "funny funy funnnny fuzzy"

# find_be = re.findall(r"fu[nz]{2}y", quote1)
# print(find_be)


# #1. search
# #2. findAll
# #3. sub


# text = "Spoiler: This movie is great, but the spoiler was unexpected. avoid sharing spoilers!"

# censor_text = re.sub(r"spoiler", "*******", text, flags = re.IGNORECASE)
# print(censor_text)


# list_websites = "facebook.com, google.com, twitter.in, amazon.com"
# #result = re.sub(r'(\w+)\.com', 'blacklist.com', list_websites)
# result = re.sub(r'(\w+)(\.com)', r'\1..subdomain\2', list_websites)
# print(result)


names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
#output = ["Doe, Jphn", "Smith, Jane", "Johnson, Alice", "Evans, Chris"]

result = []
for name in names:
 result.append(re.sub(r'(\w+)\s+(\w+)', r'\2, \1', name))
print(result)

output = [re.sub(r'(\w+)\s+(\w+)', r'\2, \1', name) for name in names]

print(output)


# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

# Output
#['#sunny', '#California', '#travel', '#fun']