#combine_code1 = merge_real_df.py + real_chi.py

#combine_code2-this_file = get_three_df_from_three_years.py + combine_code1



source_files = ["2020.txt", "2021.txt", "2022.txt"]
a = len(source_files)


for repeat in range(a):
    current_file = source_files[repeat]

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   get abstracts   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    with open(current_file, "r") as text1:
        row = "starting_value"
        this_row_belongs_to_abstract = False

        all_abstracts_words = []

        while row != "":
            row = text1.readline()
            row_cat = row.split(" ")
            #CONDITION1
            if row_cat[0] ==   "Abstract:":
                this_row_belongs_to_abstract = True
            elif row_cat[0] == "Keywords:":
                this_row_belongs_to_abstract = False
            elif row ==        "\n":
                this_row_belongs_to_abstract = False
            else:
                condition1 = "else1"

            #CONDITION2
            if this_row_belongs_to_abstract is True:
                all_abstracts_words = all_abstracts_words + row_cat
            else:
                condition2 = "else2"

    print("\n\n всего слов во всех абстрактах:", len(all_abstracts_words) )
    #print(all_abstracts_words)
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get abstracts   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑




    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   get titles   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    '''
    oblifrodoc2  = obtained_line_from_doc2
    liwialtiwo   = list_with_all_titles_words
    liwiwofrobli = list_with_words_from_obtained_line
    '''
    with open(current_file, "r") as doc2:
        liwialtiwo = []

        #1) для первой статьи:
        #1.1) взять вторую строку:
        oblifrodoc2 = doc2.readline()#это первая строка
        oblifrodoc2 = doc2.readline()#это вторая строка
        #1.2) разделить на слова:
        liwiwofrobli = oblifrodoc2.split(" ")
        #1.3) сохранить в общий список:
        liwialtiwo = liwialtiwo + liwiwofrobli

        #для последующих статей - цикл
        #между статьями: "\n"
        #title - во второй строке после "\n"
        while oblifrodoc2 != "": #это до конца текстового файла
            oblifrodoc2 = doc2.readline()
            #CONDITION3
            if oblifrodoc2 == "\n":#это значит что я на строчке-разрыве между статьями
                oblifrodoc2 = doc2.readline()#отсчитываю первую строчку после разрыва
                oblifrodoc2 = doc2.readline()#отсчитываю вторую строчку после разрыва
                # разделить на слова:
                liwiwofrobli = oblifrodoc2.split(" ")
                # сохранить в общий список:
                liwialtiwo = liwialtiwo + liwiwofrobli #сохраняю в общий список
            else:
                condition3 = "else3"

    print("\n\n всего слов во названиях:", len(liwialtiwo) )
    #print(liwialtiwo)
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get titles   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑






    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   summation   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    abstracts_AND_titles_words = all_abstracts_words + liwialtiwo
    print("\n\n всего слов в названиях И абстрактах:", len(abstracts_AND_titles_words) )



    from collections import Counter
    words_repeat1 = dict(Counter(abstracts_AND_titles_words))
    print(words_repeat1)

    import pandas as pd
    df1 = pd.DataFrame.from_dict(words_repeat1, orient = 'index')
    print(df1)
    df1.to_csv(str(current_file)+".csv")
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   summation   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

#end_of_file



    
#merge real df.py + real_chi.py

import pandas as pd
#create df
df_20 = pd.read_csv(str(source_files[0])+".csv")
df_21 = pd.read_csv(str(source_files[1])+".csv")
df_22 = pd.read_csv(str(source_files[2])+".csv")
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

observed = merged_df_cl2.iloc[year_2020]
observed = observed.to_numpy()
observed = np.delete(observed, [0])
print("распределение_1:", observed)

expected = merged_df_cl2.iloc[year_2021]
expected = expected.to_numpy()
expected = np.delete(expected, [0])
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

statistic, pvalue = chisquare((observed), reduced_expected)
print("\n",statistic, pvalue)

if pvalue <= 0.05:
    print("reject H0,", "различаются")
else:
    print("мы не обнаружили значимых различий")



import matplotlib.pyplot as plt

plt.plot(observed, color="blue",        label="observed")
plt.plot(expected, color="red",          label="expected до")
plt.plot(reduced_expected, color="green", label="expected после деления на коэффициент")
plt.legend()
plt.show()





