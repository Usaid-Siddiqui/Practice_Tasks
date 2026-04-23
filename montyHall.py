import math
import os
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

def game():
    doors = [0] * 3
    prize_idx = random.randint(0,2)
    doors[prize_idx] = 1

    user_pick = 0

    if not doors[1]:
        doors.pop(1)
    else:
        doors.pop(2)


    return doors[0], doors[1]

total_without_changing = 0
total_with_changing = 0
with_rates = []
without_rates = []

events = int(sys.argv[1])

for i in range(events):
    x,y = game()
    total_without_changing += x
    total_with_changing += y
    with_rates.append(total_with_changing)
    without_rates.append(total_without_changing)

print("With Changing: ", total_with_changing)
print("Without Changing: ", total_without_changing)

plt.figure(figsize=(10, 5))
plt.plot(with_rates, label = "Switch", color = "blue")
plt.plot(without_rates, label = "Stay", color = "red")
plt.xlabel("Trials")
plt.ylabel("Number of Wins")
plt.title("Monty Hall Simulation")
plt.legend()
plt.tight_layout()
plt.show()