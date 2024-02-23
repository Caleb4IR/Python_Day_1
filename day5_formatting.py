from math import pi
from datetime import datetime

# now = datetime.now()
# print(now)
# print(f"The current date is: {now:%d-%m-%Y}")
# print(f"The current date is: {now:%d/%m/%Y}")
# print(f"The current date is: {now:%d/%m/%Y}")

# salary = 420_000_000
# print(salary)# For DX

# print(f"Dhara's salary is R{salary:,}")
# print(f"Dhara's salary is R{salary:_}")

# print(f"The PI value is {pi}")
# print(f"The PI value is {pi:.2f}")
# print(f"The PI value is {pi:.3f}")

name = "Lilitha"
person = "Quinlan"
print(f"{name:>20}")
print(f"{name:<20}:")
print(f"{name:^20}:")

print(f"{person:*>20}:")
print(f"{person:#<20}:")
print(f"{person:$^20}:")

# caleb = 0.925
# print(f"The test results are out and Caleb got {caleb:.2%}")

about_me = """
Hi, My name is Caleb
I stay at Cape Town
"""

print(about_me)
