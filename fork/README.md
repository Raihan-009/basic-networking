# Fork( )

<p> <span style = "font-weight : Bold"> Keywords : </span> Concurrency, Unix, Pid </p>

<p style = "text-align : justify"> <span style = "font-weight : Bold">Concurrency :</span> Concurrency means multiple computations are happening at the same time. In others word Concurrency is the OS’s ability to execute multiple instructions simultaneously. Fork() enables this concurrency. </p>

<p style = "text-align : justify"> <span style = "font-weight : Bold">Unix :</span> Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix. </p>

<p style = "text-align : justify"> <span style = "font-weight : Bold">Pid :</span> Here Pid stands for Process Id. It refers a unique process identifier. Upon successful completion, fork() returns 0 to the child process and returns the process ID of the child process to the parent process. Otherwise, -1 is returned to the parent process, no child process is created, and errno is set to indicate the error.</p>

<p style = "text-align : justify">Fork() is a method how we create new processes in Unix. When we call fork, actually we create a copy of our own process with its own address space. Multiple tasks can be handled independently using the fork's working process, which is similar to the multiverse notion. 
Essentially, fork duplicates the currently running process, which is referred to as the parent process and the child process. And both processes will independently run the script from the first line to the last. They do not have any idea about existance of other process. </p>

Code Example : 

```python
import os

print("Process - 01 has executed.")
```

OUTPUT:
```
Process - 01 has executed.
```
<p>As there was just one process, we only got one output.</p>

<p>Let's have a look at what happens if we use fork().</p>

```python
import os 

process_no = 1

PID = os.fork()
print(f'Process No 1 has executed & respective PID is {PID}')
```
OUTPUT:
```
Process No 1 has executed & respective PID is 3463
Process No 1 has executed & respective PID is 0
```
<p>And we got exactly the same result twice, with two different PID values! The first corresponds to the parent process, and we see that the pid number is larger than 0. The second corresponds to the child process, for which we received a pid number of 0.</p>

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