# combine_code1 = merge_real_df.py + real_chi.py
# combine_code2-this_file = get_three_df_from_three_years.py + combine_code1

source_files = ["2020.txt", "2021.txt"]
file_1_name = str(source_files[0])
file_2_name = str(source_files[1])

for current_file in source_files:
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   get abstracts   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    with open(current_file, "r") as text1:
        row = "starting_value"
        this_row_belongs_to_abstract = False
        all_abstracts_words = []
        while row != "":
            row = text1.readline()
            row_cat = row.split(" ")
            # CONDITION1
            if row_cat[0] == "Abstract:":
                this_row_belongs_to_abstract = True
            elif row_cat[0] == "Keywords:":
                this_row_belongs_to_abstract = False
            elif row == "\n":
                this_row_belongs_to_abstract = False
            else:
                condition1 = "else1"
            # CONDITION2
            if this_row_belongs_to_abstract is True:
                all_abstracts_words = all_abstracts_words + row_cat
            else:
                condition2 = "else2"
    print("\n", "в файле", current_file, "кол-во слов во всех абстрактах:", len(all_abstracts_words))
    # print("\n", "файл:", current_file, "текст всех абстрактов:", all_abstracts_words)
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get abstracts   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   get titles   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # oblifrodoc2  = obtained_line_from_doc2
    # liwialtiwo   = list_with_all_titles_words
    # liwiwofrobli = list_with_words_from_obtained_line
    with open(current_file, "r") as doc2:
        liwialtiwo = []
        # 1) для первой статьи:
        # 1.1) взять вторую строку:
        oblifrodoc2 = doc2.readline()  # это первая строка
        oblifrodoc2 = doc2.readline()  # это вторая строка
        # 1.2) разделить на слова:
        liwiwofrobli = oblifrodoc2.split(" ")
        # 1.3) сохранить в общий список:
        liwialtiwo = liwialtiwo + liwiwofrobli
        # 2) для последующих статей - цикл
        # между статьями: "\n"
        # title - во второй строке после "\n"
        while oblifrodoc2 != "":  # это до конца текстового файла
            oblifrodoc2 = doc2.readline()
            # CONDITION3
            if oblifrodoc2 == "\n":  # это значит что я на строчке-разрыве между статьями
                oblifrodoc2 = doc2.readline()  # отсчитываю первую строчку после разрыва
                oblifrodoc2 = doc2.readline()  # отсчитываю вторую строчку после разрыва
                # разделить на слова:
                liwiwofrobli = oblifrodoc2.split(" ")
                # сохранить в общий список:
                liwialtiwo = liwialtiwo + liwiwofrobli  # сохраняю в общий список
            else:
                condition3 = "else3"
    print("\n", "в файле", current_file, "кол-во слов в заголовках:", len(liwialtiwo))
    # print("\n", "файл:", current_file, "все заголовки:", liwialtiwo)
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get titles   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   summation   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    abstracts_AND_titles_words = all_abstracts_words + liwialtiwo
    print("\n", "в файле", current_file, "кол-во слов в названиях И абстрактах:", len(abstracts_AND_titles_words))

    # очистка слов в list от всех символов
    # https://www.educative.io/answers/what-is-the-numpychartranslate-function-in-python
    # https://www.w3resource.com/numpy/string-operations/index.php
    import numpy as np

    for cleaning in range(1):
        all_words_ndarray1 = np.array(abstracts_AND_titles_words)
        # print( type(all_words_ndarray1), "содержит:", all_words_ndarray1.dtype)
        my_dict1 = {":": "", ".": "", ",": "", "(": "", ")": "",
                    "&": "", "[": "", "]": "", "±": "", ">": "",
                    "<": "", " ": "", "=": "", "±": "", ";": "",
                    "+": "", "“": "", "”": "", "~": "", "{": "",
                    "}": "", "\n": "", }  # "%" : "" , "'s" : "" ,
        my_table1 = "monkey".maketrans(my_dict1)
        all_words_ndarray1_cl = np.char.translate(all_words_ndarray1, my_table1, deletechars=None)
        # сделать все буквы маленькими
        all_words_ndarray1_cl_lo = np.char.lower(all_words_ndarray1_cl)
        # заканчиваю встраивание "очищающего кода":
        abstracts_AND_titles_words = all_words_ndarray1_cl_lo
        print(type(abstracts_AND_titles_words), "содержит:", abstracts_AND_titles_words.dtype)

    from collections import Counter

    words_repeat1 = dict(Counter(abstracts_AND_titles_words))
    # print("\n", "файл:", current_file, "словарь:", words_repeat1)

    import pandas as pd

    df1 = pd.DataFrame.from_dict(words_repeat1, orient='index')
    print(df1)
    df1.to_csv(str(current_file) + ".csv")
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   summation   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

# end_of_file


# merge real df.py + real_chi.py

import pandas as pd

# create df
df_20 = pd.read_csv(file_1_name + ".csv")
df_21 = pd.read_csv(file_2_name + ".csv")

# задать названия колонок
hamburger1 = "ВСТРЕТИЛОСЬ РАЗ в файле " + file_1_name
hamburger2 = "ВСТРЕТИЛОСЬ РАЗ в файле " + file_2_name
df_20.columns = ["СЛОВО", hamburger1]
df_21.columns = ["СЛОВО", hamburger2]

# перевернуть таблицы
#
df20_tr = df_20.transpose()
df20_tr.to_csv(file_1_name + "_tr" + ".csv")
#
df21_tr = df_21.transpose()
df21_tr.to_csv(file_2_name + "_tr" + ".csv")

# отредактировать таблицы - вынести колонки
#
with open(file_1_name + "_tr.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()
    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    csvtext1.close()
new_file = open(file_1_name + "_tr_col.csv", 'w')
new_file.write(csv_str1)
new_file.close()
df_20_tr_col = pd.read_csv(file_1_name + "_tr_col.csv")
#
with open(file_2_name + "_tr.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()
    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    csvtext1.close()
new_file = open(file_2_name + "_tr_col.csv", 'w')
new_file.write(csv_str1)
new_file.close()
df_21_tr_col = pd.read_csv(file_2_name + "_tr_col.csv")

# объединение датафреймов
merged_df = pd.concat([df_20_tr_col, df_21_tr_col])
print(merged_df)
merged_df.to_csv("merged_df.csv")

import numpy as np
import pandas as pd
import scipy.stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency

# имя merged не нужно повторять!(все-таки надо - появляется колонка)
merged_df = pd.read_csv("merged_df.csv")
# print(merged_df.info())
# print("*"*30)

# clean
merged_df_cl = merged_df.dropna(axis=1)
print(merged_df_cl.info())
print("*" * 30)
merged_df_cl.to_csv("merged_df_cl.csv")
# пустая колонка в начале образоовалась - удалить
merged_df_cl2 = merged_df_cl.drop("Unnamed: 0", axis=1)
merged_df_cl2.to_csv("merged_df_cl2.csv")

# выделить распределения
#
distr_of_file_1_ser = merged_df_cl2.iloc[0]
distr_of_file_1_ndar = distr_of_file_1_ser.to_numpy()
distr_of_file_1_fin = np.delete(distr_of_file_1_ndar, [0])
# print("распределение__of_file_1:", distr_of_file_1)
#
distr_of_file_2_ser = merged_df_cl2.iloc[1]
distr_of_file_2_ndar = distr_of_file_2_ser.to_numpy()
distr_of_file_2_fin = np.delete(distr_of_file_2_ndar, [0])
# print("распределение__of_file_2:", distr_of_file_2)

# коэф на который нужно уменьшить каждое число,
# чтобы сумма слов была одинаковая
# слова распределяются так_1 и так_2
distr_of_file_1_s = sum(distr_of_file_1_fin)
distr_of_file_2_s = sum(distr_of_file_2_fin)

print("\n", distr_of_file_1_s, distr_of_file_2_s)
avgsum = (distr_of_file_1_s + distr_of_file_2_s) / 2
print(avgsum)
#
coef20 = avgsum / distr_of_file_1_s  # коэф для _of_file_1
coef21 = avgsum / distr_of_file_2_s  # коэф для _of_file_2
#
distr_of_file_1_coef = distr_of_file_1_fin * coef20
distr_of_file_2_coef = distr_of_file_2_fin * coef21
#
print("распределение_" + file_1_name + "_коэф:", distr_of_file_1_coef)
print("распределение_" + file_2_name + "_коэф:", distr_of_file_2_coef)

# print("распределение_2:", reduced_expected)
# reduced_expected_r = np.around(reduced_expected.astype(np.double), 2)
# print("распределение_2_коэф:", reduced_expected_r)


statistic, pvalue = chisquare(distr_of_file_1_coef, distr_of_file_2_coef)
print("\n", statistic, pvalue)

if pvalue <= 0.05:
    print("reject H0,", "различаются")
else:
    print("мы не обнаружили значимых различий")

###
import scipy
from scipy import stats

cor, pval = stats.spearmanr(distr_of_file_1_coef, distr_of_file_2_coef)
print(pval)
if pval < 0.05:
    print("есть доказательства связи")
else:
    print("нет доказательств связи")
###

import matplotlib.pyplot as plt

print_real = True  #
if print_real is True:
    plt.plot(distr_of_file_1_fin, color="blue", label="distribution_" + file_1_name + "_real")
    plt.plot(distr_of_file_2_fin, color="red", label="distribution_" + file_2_name + "_real")
else:
    plt.plot(distr_of_file_1_coef, color="blue", label="distribution_" + file_1_name + "_coef")
    plt.plot(distr_of_file_2_coef, color="red", label="distribution_" + file_2_name + "_coef")

plt.legend()
plt.show()





