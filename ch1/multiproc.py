# Let's play around with Python's Multiprocessing
# https://docs.python.org/3/library/multiprocessing.html

# Spawn processes using API similar to the
# Threading module - https://docs.python.org/3/library/threading.html#module-threading

# Offers local and remote concurrency on Windows and POSIX compliant OSs

# Uses subprocesses to side step global interpreter lock

# Global Interpreter Lock - https://docs.python.org/3/glossary.html#term-global-interpreter-lock
#
# By default, CPython locks system so only one thread may be running Python byte code at a time preventing concurrent access to records like `dict`
# This is turned off, or side stepped (Multiprocessing module sidesteps) in some instances to enable truly parallel workflows

# Pool
# - Parallelize execution across multiple input values

from multiprocessing import Pool

def f(x):
  return x*x

if __name__ == '__main__':
  with Pool(5) as p:
    print(p.map(f, [1, 2, 3]))

# Multiprocessing Guidelines (https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming)

# Avoid shared state (between procs) - Don't use Erlang for video processing, got it!

# Use queues or pipes instead of low level sync to communicate between procs

# Ensure arguments serialize and deserialize with Pickle module (https://docs.python.org/3/library/pickle.html) - Object -> byte stream and vice versa

# Don't access proxy objects from more than one thread unless using a lock
