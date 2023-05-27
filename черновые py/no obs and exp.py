import pandas as pd
import numpy as np
merged_df_cl2 = pd.read_csv("merged_df_cl.csv")

#почему-то при чтении csv возникают уже две пустые колонки
print(merged_df_cl2.head(), "\n")

#выделить распределения
year_2020 = 0
year_2021 = 1
year_2022 = 2
#
distribution_2020 = merged_df_cl2.iloc[year_2020]
distribution_2020 = distribution_2020.to_numpy()
#почему-то при чтении csv возникают уже две пустые колонки
distribution_2020 = np.delete(distribution_2020, [0, 1, 2]) #поэтому индексы!
#print("распределение_2020:", distribution_2020)
#
distribution_2021 = merged_df_cl2.iloc[year_2021]
distribution_2021 = distribution_2021.to_numpy()
#почему-то при чтении csv возникают уже две пустые колонки
distribution_2021 = np.delete(distribution_2021, [0, 1, 2]) #поэтому индексы!
#print("распределение_2021:", distribution_2021)
#
distribution_2022 = merged_df_cl2.iloc[year_2022]
distribution_2022 = distribution_2022.to_numpy()
#почему-то при чтении csv возникают уже две пустые колонки
distribution_2022 = np.delete(distribution_2022, [0, 1, 2]) #поэтому индексы!
#print("распределение_2022:", distribution_2022)
#коэф на который нужно уменьшить каждое число,
#чтобы сумма слов была одинаковая
#слова распределяются так_1 и так_2
distr2020_s = sum(distribution_2020)
distr2021_s = sum(distribution_2021)
distr2022_s = sum(distribution_2022)
print("\n", distr2020_s, distr2021_s, distr2022_s)
avgsum = (distr2020_s + distr2021_s + distr2022_s)/3
print(avgsum)
#
coef20 = avgsum/distr2020_s #коэф для 2020
coef21 = avgsum/distr2021_s #коэф для 2021
coef22 = avgsum/distr2022_s #коэф для 2022
#
distribution_2020_coef = distribution_2020 * coef20
distribution_2021_coef = distribution_2021 * coef21
distribution_2022_coef = distribution_2022 * coef22
#
print("распределение_2020_коэф:", distribution_2020_coef)
print("распределение_2021_коэф:", distribution_2021_coef)
print("распределение_2022_коэф:", distribution_2022_coef)

'''
print("распределение_2:", reduced_expected)
reduced_expected_r = np.around(reduced_expected.astype(np.double), 2)
print("распределение_2_коэф:", reduced_expected_r)
'''
import matplotlib.pyplot as plt
print_real = True
if print_real is True:
    plt.plot(distribution_2020, color="blue", label="distribution_2020_real")
    plt.plot(distribution_2021, color="red", label="distribution_2021_real")
    plt.plot(distribution_2022, color="green", label="distribution_2022_real")
else:
    plt.plot(distribution_2020_coef, color="blue", label="distribution_2020_coef")
    plt.plot(distribution_2021_coef, color="red", label="distribution_2021_coef")
    plt.plot(distribution_2022_coef, color="green", label="distribution_2022_coef")

plt.legend()
plt.show()

