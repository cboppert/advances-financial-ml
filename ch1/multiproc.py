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

# Best to join all processes in order to ensure they do not become zombies (POSIX term for processes which are completed but not yet joined)... that being said, if you do not join a process most will be joined automatically when a new process starts, or on an `is_alive` check

# Better to inherit then serialize/deserialize with the Pickle format and using pipes or queues to share data. Seems like processes can have ancestor processes so there must be some way of cascading scope down

# Avoid terminating processes which can cause locks and semaphores to end up in a broken, unreleased state. Only use Process.terminate on processes which do not use shared resources

# Joining is the equivalent of "await"ing threads. I.E. join will wait for a thread to call pthread_exit

# Joining can return a value

# Joining and exiting will free up all resources associated with the thread

# when joining a process which uses a queue, all queue items must have been pushed out through underlying pipe, or process will not terminate and join will never occur

# Explicitly pass resources to child threads when using "fork" start method. Better than using a shared global resource created in parent. May make code compatible with Windows, also ensures object will not be GC'd as long as child process alive

# ```python bad
#   from multiprocessing import Process, Lock
#   
#   def f():
#     ... do something with lock, which is globally defined below
#
#   if __name__ = '__main__':
#     lock = Lock()
#     for i in range(10):
#       Process(target=f).start()

# lock is defined globally there! But will be cleaned up when main process is finished even if child
# process is still relying on that lock

# Instead...

# ```python good
#   from multiprocessing import Process, Lock
#   
#   def f(l):
#     ... do something with l, which is globally defined below
#
#   if __name__ = '__main__':
#     lock = Lock()
#     for i in range(10):
#       Process(target=f, args=(lock,)).start()

# Beware of replacing sys.stdin with a file like object. Make fork safe by storing PID when appending to cache, and discarding when pid changes
