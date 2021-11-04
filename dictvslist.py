import sys
import timeit
import random

N = int(sys.argv[1])

# Initialize our objects
my_list = list()
my_dict = dict()

for i in range(N):
    val = random.uniform(0, 1)
    my_list.append([i, val])
    my_dict.update({i: val})
    
# How big are they?
print(f"List size: {sys.getsizeof(my_list)}")
print(f"Dict size: {sys.getsizeof(my_dict)}")


# Check lookups
M = int(sys.argv[2])

lookups = random.sample(list(range(N)), M)

ltime = '''
list_vals = []
for i in lookups:
    for j in my_list:
        if i == j[0]:
            list_vals.append(j[1])
        else:
            continue
'''

dtime = '''
dict_vals = []
for i in lookups:
    if i in my_dict.keys():
       dict_vals.append(my_dict[i])
    else:
        continue
'''

lt = timeit.timeit(stmt=ltime, number=10, globals=globals())
dt = timeit.timeit(stmt=dtime, number=10, globals=globals())

print(f"List lookup time: {lt}")
print(f"Dict lookup time: {dt}")