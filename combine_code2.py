# combine_code1 = merge_real_df.py + real_chi.py
# combine_code2-this_file = get_three_df_from_three_years.py + combine_code1
import pandas as pd
import numpy as np

import scipy.stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency

import scipy
from scipy import stats

import matplotlib.pyplot as plt

stars = '\n' + str('*' * 90)

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
    print("в файле", current_file, "кол-во слов во всех абстрактах:", len(all_abstracts_words))
    # print("\n", "файл:", current_file, "текст всех абстрактов:", all_abstracts_words, '\n')
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
    print("в файле", current_file, "кол-во слов в заголовках:", len(liwialtiwo))
    # print("\n", "файл:", current_file, "все заголовки:", liwialtiwo, '\n')
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get titles   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   summation   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    abstracts_AND_titles_words = all_abstracts_words + liwialtiwo
    print("в файле", current_file, "кол-во слов в названиях И абстрактах:", len(abstracts_AND_titles_words), '\n')

    # очистка слов в list от всех символов
    # https://www.educative.io/answers/what-is-the-numpychartranslate-function-in-python
    # https://www.w3resource.com/numpy/string-operations/index.php
    abst_n_titl_wordsndarray1 = np.array(abstracts_AND_titles_words)
    # print( type(abst_n_titl_wordsndarray1), "содержит:", abst_n_titl_wordsndarray1.dtype, '\n')
    
    my_dict1 = {":": "",  ".": "",  ",": "",  "(": "", ")": "",
                "&": "",  "[": "",  "]": "",  "±": "", ">": "",
                "<": "",  " ": "",  "=": "",  "±": "", ";": "",
                "+": "",  "“": "",  "”": "",  "~": "", "{": "",
                "}": "",  "\n": "", }  # "%" : "" , "'s" : "" ,
    my_table1 = "monkey".maketrans(my_dict1)
    abst_n_titl_wordsndarray1_cl = np.char.translate(abst_n_titl_wordsndarray1, my_table1, deletechars=None)

    # сделать все буквы маленькими
    abst_n_titl_wordsndarray1_cl_lo = np.char.lower(abst_n_titl_wordsndarray1_cl)
    print("ndarray со всеми словами заглавий и абстрактов файла",current_file,
          type(abst_n_titl_wordsndarray1_cl_lo), "содержит:", abst_n_titl_wordsndarray1_cl_lo.dtype, '\n')

    from collections import Counter
    words_repeat1 = dict(Counter(abst_n_titl_wordsndarray1_cl_lo))
    # print("\n", "файл:", current_file, "словарь:", words_repeat1, '\n')

    df1 = pd.DataFrame.from_dict(words_repeat1, orient='index')
    print("датафрейм для файла", current_file, '-> сохранение в csv \n', df1.head(), stars)
    df1.to_csv(str(current_file) + ".csv")
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   summation   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# end_of_file


# merge real df.py + real_chi.py
# create df
df_of_file_1 = pd.read_csv(file_1_name + ".csv")
df_of_file_2 = pd.read_csv(file_2_name + ".csv")
print("вертикальный датафрейм файла_1 \n", df_of_file_1.head(), stars)
print("вертикальный датафрейм файла_2 \n", df_of_file_2.head(), stars)

# задать названия колонок
hamburger1 = "ВСТРЕТИЛОСЬ РАЗ в файле " + file_1_name
hamburger2 = "ВСТРЕТИЛОСЬ РАЗ в файле " + file_2_name
df_of_file_1.columns = ["СЛОВО", hamburger1]
df_of_file_2.columns = ["СЛОВО", hamburger2]

# перевернуть таблицы
#
df_of_file_1_tr = df_of_file_1.transpose()
df_of_file_1_tr.to_csv(file_1_name + "_tr" + ".csv")
print("горизонтальный датафрейм файла_1 -> в csv \n", df_of_file_1_tr.head(), stars)
#
df_of_file_2_tr = df_of_file_2.transpose()
df_of_file_2_tr.to_csv(file_2_name + "_tr" + ".csv")
print("горизонтальный датафрейм файла_2 -> в csv \n", df_of_file_2_tr.head(), stars)

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
df_of_file_1_tr_col = pd.read_csv(file_1_name + "_tr_col.csv")
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
df_of_file_2_tr_col = pd.read_csv(file_2_name + "_tr_col.csv")

# объединение датафреймов
merged_df = pd.concat([df_of_file_1_tr_col, df_of_file_2_tr_col])
print("объединенные датафреймы -> csv \n", merged_df, stars)
merged_df.to_csv("merged_df.csv")

# имя merged не нужно повторять!(все-таки надо - появляется колонка)
merged_df = pd.read_csv("merged_df.csv")
# print(merged_df.info(), stars)

# clean
merged_df_cl = merged_df.dropna(axis=1)
print(merged_df_cl.info(), stars)

merged_df_cl.to_csv("merged_df_cl.csv")
# пустая колонка в начале образоовалась - удалить
merged_df_cl2 = merged_df_cl.drop("Unnamed: 0", axis=1)
merged_df_cl2.to_csv("merged_df_cl2.csv")

# выделить распределения
#
distr_of_file_1_ser = merged_df_cl2.iloc[0]
distr_of_file_1_ndar = distr_of_file_1_ser.to_numpy()
distr_of_file_1_fin = np.delete(distr_of_file_1_ndar, [0])
# print("распределение__of_file_1:", distr_of_file_1, stars)
#
distr_of_file_2_ser = merged_df_cl2.iloc[1]
distr_of_file_2_ndar = distr_of_file_2_ser.to_numpy()
distr_of_file_2_fin = np.delete(distr_of_file_2_ndar, [0])
# print("распределение__of_file_2:", distr_of_file_2, stars)

# коэф на который нужно уменьшить каждое число,
# чтобы сумма слов была одинаковая
# слова распределяются так_1 и так_2
distr_of_file_1_s = sum(distr_of_file_1_fin)
distr_of_file_2_s = sum(distr_of_file_2_fin)

print(distr_of_file_1_s, distr_of_file_2_s, stars)
avgsum = (distr_of_file_1_s + distr_of_file_2_s) / 2
print(avgsum, '\n')
#
coef_for_file_1 = avgsum / distr_of_file_1_s  # коэф для _of_file_1
coef_for_file_2 = avgsum / distr_of_file_2_s  # коэф для _of_file_2
#
distr_of_file_1_coef = distr_of_file_1_fin * coef_for_file_1
distr_of_file_2_coef = distr_of_file_2_fin * coef_for_file_2
#
print("распределение_" + file_1_name + "_коэф:", distr_of_file_1_coef)
print("распределение_" + file_2_name + "_коэф:", distr_of_file_2_coef, stars)

#так округлять:
# _____r = np.around(___.astype(np.double), 2)



statistic, pvalue = chisquare(distr_of_file_1_coef, distr_of_file_2_coef)
print(statistic, pvalue)

if pvalue <= 0.05:
    print("reject H0,", "различаются", stars)
else:
    print("мы не обнаружили значимых различий", stars)

###
cor, pval = stats.spearmanr(distr_of_file_1_coef, distr_of_file_2_coef)
print(pval)
if pval < 0.05:
    print("есть доказательства связи", stars)
else:
    print("нет доказательств связи", stars)
###


plot_real = True  #
if plot_real is True:
    plt.plot(distr_of_file_1_fin, color="blue", label="distribution of " + file_1_name + " real")
    plt.plot(distr_of_file_2_fin, color="red", label="distribution of " + file_2_name + " real")
else:
    plt.plot(distr_of_file_1_coef, color="blue", label="distribution of " + file_1_name + " coef")
    plt.plot(distr_of_file_2_coef, color="red", label="distribution of " + file_2_name + " coef")

plt.legend()
plt.show()






