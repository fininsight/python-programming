# package import
import pkcalc.calc

print(pkcalc.calc.add(5, 6))
print(pkcalc.calc.sub(5, 6))

# package from import
from pkcalc.calc import add, sub
print(add(5, 6))
print(sub(5, 6))

"""
from pkcalc import *
print(add(5, 6))
print(sub(5, 6))
"""
