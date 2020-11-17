# check_images.py

# TODO: 0: Timing Code
# Name: Yusuke Aita
# The date I started working on this project: 16th of November

# Imports time() and sleep() fucntions from time module
from time import time, sleep

# Sets start time
start_time = time()

# Replace sleep (75) below with code you want to start_time
sleep(75)

# Sets end time
end_time = time()

# Computes overall runtime in seconds
tot_time = start_time - end_time

print("start time: {}, end time: {}, tot-time: {}".format(start_time, end_time, tot_time))

# Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
