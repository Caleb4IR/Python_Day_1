#Print secret message after the 🔑
# message = "    🚨🔍📱🔑secret_code✌️"
# code = "SECRET_CODE✌️"

# key_idx = message.find("🔑")
# print(key_idx)
# secret_msg = message[(key_idx+1):]
# output = secret_msg.upper()


# if(output == code):
#   print("You have unlocked the secret code")
# else:
#   print("You have not unlocked the secret code")

#Task 2: 
# If the key is not present you must get no secret is present
# message = "    🚨🔍📱secret_code✌️"
# code = "SECRET_CODE✌️"

# key_idx = message.find("🔑")
# secret_msg = message[(key_idx+1):]
# output = secret_msg.upper()

# if(output == code):
#   print("You have unlocked the secret code")
# elif ("🔑" not in message):
#   print("No secret is present")
# else:
#   print("You have not unlocked the secret code")

#Task 3
# message = "    🚨🔍📱🔑****secret_code✌️((("
# code = "SECRET_CODE✌️"

# key_idx = message.find("🔑")
# secret_msg = message[(key_idx+1):]

# fix_msg = secret_msg.strip("*")
# fix_more = fix_msg.strip("(")
# output = fix_more.upper()

# if(output == code):
#   print("You have unlocked the secret code")
# elif ("🔑" not in message):
#   print("No secret is present")
# else:
#   print("You have not unlocked the secret code")

#You can dot chain
message = "    🚨🔍📱🔑****secret_code✌️((("
code = "SECRET_CODE✌️"

key_idx = message.find("🔑")
secret_msg = message[(key_idx+1):]

output = secret_msg.strip("*").strip("(").upper()
if(output == code):
  print("You have unlocked the secret code")
elif ("🔑" not in message):
  print("No secret is present")
else:
  print("You have not unlocked the secret code")

