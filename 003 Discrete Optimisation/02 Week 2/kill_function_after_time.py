# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 05:50:06 2017

@author: parenti daniele
"""
import multiprocessing
from multiprocessing import Queue

TIMEOUT = 5

def big_loop(bob):
    import time
    time.sleep(4)
    return bob*2

def wrapper(queue, bob):
    result = big_loop(bob)
    queue.put(result)
    queue.close()

def run_loop_with_timeout():
    bob = 21 # Whatever sensible value you need
    queue = multiprocessing.Queue(1) # Maximum size is 1
    proc = multiprocessing.Process(target=wrapper, args=(queue, bob))
    proc.start()

    # Wait for TIMEOUT seconds
    try:
        result = queue.get(True, TIMEOUT)
    except Queue.Empty:
        # Deal with lack of data somehow
        result = "No result"
    finally:
        proc.terminate()

    # Process data here, not in try block above, otherwise your process keeps running
    print(result)

if __name__ == "__main__":
    run_loop_with_timeout()
    
    #%%

import subprocess as sub
import threading

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = sub.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()      #use self.p.kill() if process needs a kill -9
            self.join()

RunCmd(["./someProg", "arg1"], 60).Run()

#%%
import multiprocessing
import time

# Your foo function
def foo(n):
    for i in range(10000 * n):
        print("Tick")
        time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    queue = multiprocessing.Queue(1)
    p = multiprocessing.Process(target=foo, name="Foo", args=(10))
    p.start()

    # Wait a maximum of 10 seconds for foo
    # Usage: join([timeout in seconds])
    p.join(10)
    
    # If thread is active
    if p.is_alive():
        print("foo is running... let's kill it...")
    
        # Terminate foo
        p.terminate()
        p.join()
        
#%%
import multiprocessing