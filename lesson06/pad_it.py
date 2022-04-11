num = 303
flt = 12.34
str = "Formatting"

#Formatting Integers
#width
print(f"Value: {num:7}")
#flags
print(f"{num:+}")
print(f"{num:08}")
print(f"{num:+08}")

#Formatting Floating-point Numbers
#width
print(f"Value: {flt:10.2f}")
print(f"Value: {flt:10.2}")
#percision
print(f"{flt:.4}")
print(f"{flt:.0f}")
print(f"{flt:.4e}")
#flags
print(f"{flt:07.2f}")

#Formatting Strings
#width
print(f"{str:20} String")
#percision
print(f"{str:.6} String")
#flags
print(f"{str:>20} String")
