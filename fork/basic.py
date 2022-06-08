from imghdr import what
import os 


process_no = 1

whatever = os.fork()
print(type(whatever))


print(whatever)

print("Process " + str(process_no))