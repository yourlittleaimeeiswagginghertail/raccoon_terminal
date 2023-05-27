#merge real df.py + real_chi.py

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

import numpy as np
import pandas as pd
import scipy.stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
#имя merged не нужно повторять!(все-таки надо - появляется колонка)
merged_df = pd.read_csv("merged_df.csv")
#print(merged_df.info())
#print("*"*30)

#clean
merged_df_cl = merged_df.dropna(axis=1)
print(merged_df_cl.info())
print("*"*30)
merged_df_cl.to_csv("merged_df_cl.csv")
#пустая колонка в начале образоовалась - удалить
merged_df_cl2 = merged_df_cl.drop("Unnamed: 0", axis=1)
merged_df_cl2.to_csv("merged_df_cl2.csv")

#выделить распределения
year_2020 = 0
year_2021 = 1
year_2022 = 2

observed = merged_df_cl2.iloc[year_2021]
observed = observed.to_numpy()
observed = np.delete(observed, [0])
print("распределение_1:", observed)

expected = merged_df_cl2.iloc[year_2022]
expected = expected.to_numpy()
expected = np.delete(expected, [0])

#коэф на который нужно уменьшить каждое число,
#чтобы сумма слов была одинаковая
#слова распределяются так_1 и так_2
obs_words = sum(observed)
exp_words = sum(expected)
x = exp_words / obs_words
reduced_expected = expected / x
print("распределение_2:", reduced_expected)

statistic, pvalue = chisquare((observed), reduced_expected)
print("\n",statistic, pvalue)

if pvalue <= 0.05:
    print("reject H0,", "различаются")
else:
    print("мы не обнаружили значимых различий")












