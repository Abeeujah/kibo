import random, time

# TODO 1: Print a welcome message. Include "press Enter to start".
print("press Enter to start")
# TODO 2: use input() to wait for the user to press Enter
input()
# TODO 3: wait a random number of seconds, then print "DRAW!"
time.sleep(random.randint(1, 5))
print("DRAW")
# TODO 4: Time how long it takes for the user to press Enter. Get the current time with time.time()
start_time = time.time()
# TODO 5: use input() to wait for the user to press Enter
input()
# TODO 6: Use time.time() again to get the time after the user pressed Enter
elapsed_time=time.time()
# TODO 7: Print how long it took
delta = elapsed_time - start_time
print(delta)
# TODO 8: Print different results, based on how long it took
if delta > 0.3: 
  print("Too slow! Try again next time.")
elif delta < 0.1:
  print("You pressed Enter too soon, didn't you?")
  
else:
  print("You're the fastest draw in the west, congratulations!")