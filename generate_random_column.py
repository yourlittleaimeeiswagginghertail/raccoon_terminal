import numpy as np
import pandas as pd

# рандомные integers [0 - 250)
# колонка size 50, 1
bike = np.random.randint(0, 250, size=(50, 1))
#print(bike)
#print(type(bike))

df1 = pd.DataFrame(bike, columns = ["random integers"])
print(df1)
df1.to_csv("random_integers.csv")
