# module import
import calc
print(calc.name)
print(calc.add(5, 6))

# module from import
from calc import name, add
print(name)
print(add(5, 6))

print("name : ", __name__)
if __name__ == '__main__':
    print("start")

"""
import sys
print(sys.path)
"""
