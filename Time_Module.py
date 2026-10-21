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

#Greeting according to time of the day including time of the day
if 5 <= current_hour < 12:
    print("Good morning! The current time is:", time.strftime("%H:%M:%S", local_time))
elif 12 <= current_hour < 17:
    print("Good afternoon! The current time is:", time.strftime("%H:%M:%S", local_time))
else:
    print("Good evening! The current time is:", time.strftime("%H:%M:%S", local_time))
    