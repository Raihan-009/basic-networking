import os

p = os.fork()

if p > 0:
    os.fork()
    print('Parent Process (Inside Loop) : pid  => '+str(os.getpid()))

print('Child Process (Outside Loop) : pid => '+str(os.getpid()))