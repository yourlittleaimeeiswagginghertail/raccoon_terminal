import numpy as np
import pandas as pd
import scipy.stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency

#удалить те слова которые в каком-то из годов не встречались
#имя merged не нужно повторять!
merged_df = pd.read_csv("merged_df.csv")
print(merged_df.info())
print("*"*30)
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








