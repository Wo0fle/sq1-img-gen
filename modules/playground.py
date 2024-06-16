"""This is a testing ground for the Square-1 Class."""

from virtual_sq1 import Square1

############################################################

sq1 = Square1()

print(f"\nBefore: {sq1}")
sq1.apply_alg("(1,0) / (0,-3) / (-1,0) / (3,0) / (1,0) / (0,3) / (-1,0) / (-3,0) /", True)
print(f"After: {sq1}\n")

sq1.__init__()
print("####################")

print(f"\nBefore: {sq1}")
sq1.apply_alg("/ (3,0) / (1,0) / (0,-3) / (-1,0) / (-3,0) / (1,0) / (0,3) / -1")
print(f"After: {sq1}\n")

sq1.__init__()
print("####################")

print(f"\nBefore: {sq1}")
sq1.apply_state("A3B1C2D45E6F7G8H")
print(f"After: {sq1}\n")