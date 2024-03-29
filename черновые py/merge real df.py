import pandas as pd
#create df
df_20 = pd.read_csv("2020.txt.csv")
df_21 = pd.read_csv("2021.txt.csv")
df_22 = pd.read_csv("2022.txt.csv")
#задать названия колонок
df_20.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2020"]
df_21.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2021"]
df_22.columns = ["СЛОВО", "ВСТРЕТИЛОСЬ_РАЗ_в_2022"]
#перевернуть таблицы
#
df20_tr = df_20.transpose()
df20_tr.to_csv("2020_tr.csv")
#
df21_tr = df_21.transpose()
df21_tr.to_csv("2021_tr.csv")
#
df22_tr = df_22.transpose()
df22_tr.to_csv("2022_tr.csv")
#отредактировать таблицы - вынести колонки
#
with open("2020_tr.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()
    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    csvtext1.close()
new_file = open("2020_tr_col.csv",'w')
new_file.write(csv_str1)
new_file.close()
df_20_tr_col = pd.read_csv("2020_tr_col.csv")
#
with open("2021_tr.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()
    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    csvtext1.close()
new_file = open("2021_tr_col.csv",'w')
new_file.write(csv_str1)
new_file.close()
df_21_tr_col = pd.read_csv("2021_tr_col.csv")
#
with open("2022_tr.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()
    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    csvtext1.close()
new_file = open("2022_tr_col.csv",'w')
new_file.write(csv_str1)
new_file.close()
df_22_tr_col = pd.read_csv("2022_tr_col.csv")
#объединение датафреймов
merged_df = pd.concat([df_20_tr_col, df_21_tr_col, df_22_tr_col])
print(merged_df)
merged_df.to_csv("merged_df.csv")



