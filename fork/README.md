# Fork

<p> Keywords : Concurrency, Unix, Pid </p>

Concurrency : Concurrency means multiple computations are happening at the same time. In others word Concurrency is the OS’s ability to execute multiple instructions simultaneously. Fork() enables this concurrency.

Unix : Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix.

Pid : Here Pid stands for Process Id. Upon successful completion, fork() returns 0 to the child process and returns the process ID of the child process to the parent process. Otherwise, -1 is returned to the parent process, no child process is created, and errno is set to indicate the error.

Fork() is how we create new processes in Unix. When we call fork, actually we create a copy of our own process with its own address space.

Multiple tasks can be handled independently using the fork's working process, which is similar to the multiverse notion. 

Essentially, fork duplicates the currently running process, which is referred to as the parent process and the child process. And both processes will independently run the script from the first line to the last. They do not have any idea about existance of other process.


code example : 

```python

import os

print("Process - 01")

```
Here we got the one output.

if we use fork() :

```python

import os 
whatever = os.fork()
print("Process - 01")

```

And here we got the exact same output but two times!

Example for PID :

```python 

import os

p = os.fork()

if p > 0:
    os.fork()
    print('Parent Process (Inside Loop) : pid  => '+str(os.getpid()))

print('Child Process (Outside Loop) : pid => '+str(os.getpid()))

```

Output :

```
Parent Process (Inside Loop) : pid  => 3228
Child Process (Outside Loop) : pid => 3228
Child Process (Outside Loop) : pid => 3229
Parent Process (Inside Loop) : pid  => 3230
Child Process (Outside Loop) : pid => 3230

```