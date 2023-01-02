_x = 5435
print(_x)
# Object Identity
'''
In Python, every created object identifies uniquely in Python. Python provides the guaranteed that no two objects will have the same identifier. The built-in id() function, is used to identify the object identifier. Consider the following example.
'''
a = 50
print(id(a))
print(id(534))
print(id(_x))

name = "A"
Name = "B"
naMe = "C"
NAME = "D"
n_a_m_e = "E"
_name = "F"
name_ = "G"
_name_ = "H"
na56me = "I"

print(name, Name, naMe, NAME, n_a_m_e, NAME,
      n_a_m_e, _name, name_, _name, na56me)

# Multiple Assignment
x = y = z = 56543
print(x, y, z)

