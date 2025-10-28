import random
import matplotlib.pyplot as plt
print(random.random())
print(random.randint(1,5))
print(random.uniform(1,5))

die_roll_100_trials = [random.randint(1,6) for x in range(100)]
# @title Pre-defined function to plot experimental uniform distribution
def plot_discrete(outcome_list):
  # Plot
  plt.figure(figsize=(6, 4))
  plt.hist(outcome_list, bins=range(1, 8), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
  plt.title("Discrete Uniform Distribution")
  plt.xlabel("Outcome")
  plt.ylabel("Frequency")
  plt.grid(axis='y', linestyle='--', alpha=0.6)
  plt.xticks(range(1, 7))
  plt.show()

plot_discrete(die_roll_100_trials)