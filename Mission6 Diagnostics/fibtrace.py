from diagnostic import *
from hi_graph_connect_ends import *

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

trace(fib)
fib(3)
untrace(fib)
#fib(3)
