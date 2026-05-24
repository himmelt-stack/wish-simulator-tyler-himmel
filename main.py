from simulator import run_many_simulations
import numpy as np

data = run_many_simulations(100000)

print("Average pulls:", np.mean(data))
print("Median pulls:", np.median(data))
print("Max pulls:", max(data))