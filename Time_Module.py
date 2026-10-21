#Greeting according to time of the day
import time 
timestamp = time.time()
local_time = time.localtime(timestamp)
current_hour = local_time.tm_hour

if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 17:
    print("Good afternoon!")
else:
    print("Good evening!")