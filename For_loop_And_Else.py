for i in range(5):
    print(i)
else:
    print("Loop completed successfully")


#If break statement is used inside the loop, the else block will not be executed.
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")  # This will not be printed because the loop was terminated by break   

#While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop completed successfully")

#break statement in while loop
count = 0
while count < 5:    
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("While loop completed successfully")  # This will not be printed because the loop was terminated by break