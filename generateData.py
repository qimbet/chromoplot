import random
import numpy as np
#this code is buggy in that the last value of each line is way outside of the given ranges -- typically something hugely negative

def meanFunction(x):
    x = (1/100) * (x**2) - x + 20
    return x

for _ in range(100):
        targetMean = meanFunction(_)

        # Generate 20 integer values around the target mean using a Gaussian distribution
        values = np.random.normal(loc=targetMean, scale=5, size=45).astype(int)

        # Append the values into the text file "data.txt"
        with open("data.txt", "a") as file:
            file.write(','.join(map(str, values)) + '\n')

print("data generated!")
