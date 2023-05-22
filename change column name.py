import pandas as pd

df_22 = pd.read_csv("2021.txt.csv")
print(df_22)

print(df_22.info())



print("\n\n\n\n\n")


df_22.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ РАЗ"]

print(df_22)
print(df_22.info())
