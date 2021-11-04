import timeit
import random

my_list = [random.randint(0, 1e8) for _ in range(100000)]
my_set = set(my_list)
my_list = list(my_set)

my_lookups = [random.randint(0, 1e8) for _ in range(1000)]

list_stmt = '''
for i in my_lookups:
    i in my_list
'''

set_stmt = '''
for i in my_lookups:
    i in my_set
'''

list_time = timeit.timeit(stmt=list_stmt, number=10, globals=globals())
set_time = timeit.timeit(stmt=set_stmt, number=10, globals=globals())
print(f"List time: {list_time}")
print(f"Set time: {set_time}")
