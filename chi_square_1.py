import numpy as np
import pandas as pd
import scipy.stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency

#df1 = pd.read_csv("result2sum_3 ранд expected.csv")
df1 = pd.read_csv("result2sum_4 похожее expected.csv")

column_obs = df1["observed, эмп, 2021"]
line_obs = column_obs.to_numpy()
obs_words = sum(line_obs)

column_exp = df1["expected, теор, 2022"]
line_exp = column_exp.to_numpy()
exp_words = sum(line_exp)

#коэф на который нужно уменьшить каждое число,
#чтобы сумма слов была одинаковая
#слова распределяются так_1 и так_2
x = exp_words / obs_words
reduced_line_exp = line_exp / x
#print(reduced_line_exp)
print(sum(reduced_line_exp))

statistic, pvalue = chisquare(line_obs, reduced_line_exp)
print(statistic, pvalue)

if pvalue <= 0.05:
    print("reject H0,", "различаются")
else:
    print("мы не обнаружили значимых различий")

