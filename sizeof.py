import sys
import random

sizes = [1, 100, 10000, 100000]

# Lists
list_sizes = []
for size in sizes:
    int_list = [i for i in range(size)]
    list_sizes.append(sys.getsizeof(int_list))

# Sets
set_sizes = []
for size in sizes:
    int_set = {i for i in range(size)}
    set_sizes.append(sys.getsizeof(int_set))

tup_sizes = []
for size in sizes:
    int_tup = (i for i in range(size))
    tup_sizes.append(sys.getsizeof(int_tup))
    
print(f"Lenths: {sizes}")
print(f"List sizes (bytes): {list_sizes}")
print(f"Set sizes (bytes): {set_sizes}")
print(f"Tuple sizes (bytes): {tup_sizes}")