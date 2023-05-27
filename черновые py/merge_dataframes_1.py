import pandas as pd

df21 = pd.read_csv("1 2021 в строку издветаблкотнадсовм - Sheet1.csv")
df22 = pd.read_csv("2 2022 в строку издветаблкотнадсовм - Sheet1.csv")

#print(df21)
#print(df22)


df21 = df21.rename(columns={"слово 2021":"СЛОВО"})
df22 = df22.rename(columns={"слово 2022":"СЛОВО"})


print("\n")

df_r1 = pd.concat([df21, df22])
print(df_r1)


df_r1.to_csv("df_r1.csv")

