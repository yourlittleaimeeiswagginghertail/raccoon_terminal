import pandas as pd

#задать названия колонок
df_20 = pd.read_csv("2020.txt.csv")
#df_21 = pd.read_csv("2021.txt.csv")
#df_22 = pd.read_csv("2022.txt.csv")
df_20.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2020"]
#df_21.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2021"]
#df_22.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2022"]

print("*"*10, "новое")
print(df_20.info())
#print(df_21.info())
#print(df_22.info())

'''
#перевернуть
df20_tr = df_20.transpose()
print(df20_tr)
print("\n\n\n\n", df20_tr.info())


#df21_tr = df_21.transpose()



#dfm_2020_2021 = pd.concat([df20_tr,df21_tr])
#print(dfm_2020_2021)
'''

df21 = pd.read_csv("1 2021 в строку издветаблкотнадсовм - Sheet1.csv")
df21 = df21.rename(columns={"слово 2021":"СЛОВО"})
print("*"*10, "старое")
print(df21.info())
