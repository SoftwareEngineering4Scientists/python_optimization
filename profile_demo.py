import cProfile
import pstats
import time

def func1():
    time.sleep(0.1)

def func2():
    time.sleep(0.01)
    
def func3():
    time.sleep(0.005)

def main():
    # Here's a main function with a complicated mix of functions
    for _ in range(20):
        func3()
        for _ in range(30):
            func2()
            if _ < 20:
                func1()
            else:
                func3()
    
def profile_main():
    with cProfile.Profile() as prof:
        main()
        
        stats = pstats.Stats(prof)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        
if __name__ == '__main__':
    profile_main()