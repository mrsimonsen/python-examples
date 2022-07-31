num = 303
flt = 12.34
str = "Formatting"

#Formatting Integers
#width
print(f"Value: {num:7}")
print(f"Value: {num:1}")
#types
print(f"{num:+}")
print(f"{num:08}")
print(f"{num:+08}")
print(f"{num:b}")
print(f"{num:X}")

#Formatting Floating-point Numbers
#width
print(f"Value: {flt:10.2f}")
print(f"Value: {flt:10.2}")
#precision
print(f"{flt:.4}")
#types
print(f"{flt:.0f}")
print(f"{flt:.4e}")
print(f"{flt:07.2f}")

#Formatting Strings
#width
print(f"{str:20} String")
#precision
print(f"{str:.6} String")
#align
print(f"{str:>20} String")
print(f"{str:^20} String")
