msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())


msg1 = "      Hi, all Dream is not something that you see in sleep, dream is something that does not let you sleep"
print(msg1.strip())

msg2 = "------Hi, all Dream is not something that you see in sleep, dream is something that does not let you sleep------"
print(msg2.strip("-"))
print(msg2.lstrip("-"))
print(msg2.rstrip("-"))

msg3 = "Dream is not something that you see in sleep, dream is something that does not let you sleep"

print(msg3.find("something"))

print(msg3.replace("Dream", "🛏️"))

print(msg3.count("Dream"))
print(msg3.count("Dream"))

print(msg3.startswith("Dream"))
print(msg3.endswith("sleep"))

badge_no = "4327423"
print(badge_no.isdigit())

name = "ark"
print(name.islower())

print(len(name))

