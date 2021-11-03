
from timeit import timeit
import random

N = 100000
data = [random.randint(1, 1000) for _ in range(N)]

def squarer(vals):
    vals_squared = []
    for v in vals:
        vals_squared.append(v**2)
    return vals_squared

func_stmt= '''squarer(data)'''
comp_stmt= '''[x**2 for x in data]'''

for_time = timeit(stmt=func_stmt, number=100, globals=globals())
comp_time = timeit(stmt=comp_stmt, number=100, globals=globals())
print(for_time)
print(comp_time)