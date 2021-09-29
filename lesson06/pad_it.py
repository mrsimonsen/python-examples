print("Padding with leading 0s:")
for i in range(1,11):
    print(f"The number is {i:02}")

from math import pi
print("\nPadding decimal places:")
print(f"The value of pi is {pi:.4f}")

print("\nPadding with spaces:")
for i in range(1,11):
    print(f"The number is {i:4}")

print("\nJustify with spaces:")
for i in range(6):
    print(f"{"python"[i:]:>6}")
