import pandas as pd

#задать названия колонок
df_20 = pd.read_csv("2020.txt.csv")
#df_21 = pd.read_csv("2021.txt.csv")
#df_22 = pd.read_csv("2022.txt.csv")
df_20.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2020"]
#df_21.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2021"]
#df_22.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2022"]



#перевернуть
df20_tr = df_20.transpose()
print("*"*50, "перевернут")
print(df20_tr.info())

df20_tr.to_csv("transposed.csv")
print(df20_tr.head())
#----------------------------поосле этого вручную редактировать файл




'''
with open("transposed.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()

    end = csv_str1.index("СЛОВО")

    for repl_ind in range(end):
        #first = csvstr1[0]
        csv_str1[repl_ind] = ""
        print(csv_str1)
        #csvtext1.write(csv_str2)

        
    #print(start, end)

#dfm_2020_2021 = pd.concat([df20_tr,df21_tr])
#print(dfm_2020_2021)

df_exp = pd.read_csv("transposed.csv")
print("*"*30, "эксп")
print(df_exp.info())


#print("*"*30, "новое")
#print(df_20.info())
#print(df_21.info())
#print(df_22.info())


df21 = pd.read_csv("1 2021 в строку издветаблкотнадсовм - Sheet1.csv")
df21 = df21.rename(columns={"слово 2021":"СЛОВО"})
print("*"*50, "старое")
print(df21.info())

'''
