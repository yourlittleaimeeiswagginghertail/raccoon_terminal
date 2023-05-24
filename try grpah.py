import pandas as pd
import numpy as np
merged_df_cl2 = pd.read_csv("merged_df_cl.csv")

#почему-то при чтении csv возникают уже две пустые колонки
print(merged_df_cl2.head(), "\n")

#выделить распределения
year_2020 = 0
year_2021 = 1
year_2022 = 2

observed = merged_df_cl2.iloc[year_2020]
observed = observed.to_numpy()
#почему-то при чтении csv возникают уже две пустые колонки
observed = np.delete(observed, [0, 1, 2]) #поэтому индексы!
print("распределение_1:", observed)

expected = merged_df_cl2.iloc[year_2021]
expected = expected.to_numpy()
#почему-то при чтении csv возникают уже две пустые колонки
expected = np.delete(expected, [0, 1, 2]) #поэтому индексы!
print("распределение_2_реальное:", expected)


#коэф на который нужно уменьшить каждое число,
#чтобы сумма слов была одинаковая
#слова распределяются так_1 и так_2
obs_words = sum(observed)
exp_words = sum(expected)
x = exp_words / obs_words
reduced_expected = expected / x
#print("распределение_2:", reduced_expected)
reduced_expected_r = np.around(reduced_expected.astype(np.double), 2)
print("распределение_2_коэф:", reduced_expected_r)


import matplotlib.pyplot as plt

plt.plot(observed, color="blue")
#plt.plot(expected, color="red")
plt.plot(reduced_expected, color="green")

plt.show()
