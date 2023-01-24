#Demonstrates how to unpack variable and use the .strip() string method
one, two, three = ["\tone\n", " two ", "  three  and  four    "]
print(f"'{one}' --> '{one.strip()}'")
print(f"'{two}' --> '{two.strip()}'")
print(f"'{three}' --> '{three.strip()}'")

