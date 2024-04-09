# Append an element to a Tuple using the addition (+) operator

my_tuple = ('a', 'b', 'c')

# ✅ add an element at the end of a tuple

new_tuple = my_tuple + ('d',)  # 👈️ note comma
print(new_tuple)  # 👉️ ('a', 'b', 'c', 'd')

# ------------------------------

# ✅ add an element at the beginning of a tuple

new_tuple = ('z',) + my_tuple
print(new_tuple)  # 👉️ ('z', 'a', 'b', 'c')