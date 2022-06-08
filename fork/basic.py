from imghdr import what
import os 

process_no = 1

PID = os.fork()
print(f'Process No 1 is executing & respective PID is {PID}')