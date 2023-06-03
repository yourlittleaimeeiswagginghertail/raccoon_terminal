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

stars = '\n' + str('=' * 90)

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
    # print("в файле", current_file, "кол-во слов во всех абстрактах:", len(all_abstracts_words))
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
    # print("в файле", current_file, "кол-во слов в заголовках:", len(liwialtiwo))
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get titles   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   summation   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    abstracts_AND_titles_words = all_abstracts_words + liwialtiwo
    # print("в файле", current_file, "кол-во слов в названиях И абстрактах:", len(abstracts_AND_titles_words), '\n')

    # очистка слов в list от всех символов
    # https://www.educative.io/answers/what-is-the-numpychartranslate-function-in-python
    # https://www.w3resource.com/numpy/string-operations/index.php
    abst_n_titl_wordsndarray1 = np.array(abstracts_AND_titles_words)

    my_dict1 = {
        ":": "", ".": "", ",": "", "(": "", ")": "",
        "&": "", "[": "", "]": "", "±": "", ">": "",
        "<": "", " ": "", "=": "", ";": "",
        "+": "", "“": "", "”": "", "~": "",
        "{": "", "}": "", "0": "", "1": "", "2": "", "3": "", "4": "",
        "5": "", "6": "", "7": "", "8": "", "9": "", "%": "",
        "\n": "", "·": "","-": "", 
    }
    # - /

    my_table1 = "monkey".maketrans(my_dict1)
    abst_n_titl_wordsndarray1_cl = np.char.translate(abst_n_titl_wordsndarray1, my_table1, deletechars=None)

    # сделать все буквы маленькими
    abst_n_titl_wordsndarray1_cl_lo = np.char.lower(abst_n_titl_wordsndarray1_cl)
    # print("ndarray со всеми словами заглавий и абстрактов файла", current_file, type(abst_n_titl_wordsndarray1_cl_lo), "содержит:", abst_n_titl_wordsndarray1_cl_lo.dtype, '\n')

    from collections import Counter

    words_repeat1 = dict(Counter(abst_n_titl_wordsndarray1_cl_lo))

    df1 = pd.DataFrame.from_dict(words_repeat1, orient='index')
    # print("датафрейм для файла", current_file, '-> сохранение в csv \n', df1.head(), stars)
    df1.to_csv(str(current_file) + ".csv")
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   summation   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# end_of_file


# merge real df.py + real_chi.py
# create df
df_of_file_1 = pd.read_csv(file_1_name + ".csv")
df_of_file_2 = pd.read_csv(file_2_name + ".csv")
# print("вертикальный датафрейм файла_1 \n", df_of_file_1.head(), stars)
# print("вертикальный датафрейм файла_2 \n", df_of_file_2.head(), stars)

# задать названия колонок
hamburger1 = "in " + file_1_name
hamburger2 = "in " + file_2_name
df_of_file_1.columns = ["СЛОВО", hamburger1]
df_of_file_2.columns = ["СЛОВО", hamburger2]

# перевернуть таблицы
#
df_of_file_1_tr = df_of_file_1.transpose()
df_of_file_1_tr.to_csv(file_1_name + "_tr.csv")
# print("горизонтальный датафрейм файла_1 -> в csv \n", df_of_file_1_tr.head(), stars)
#
df_of_file_2_tr = df_of_file_2.transpose()
df_of_file_2_tr.to_csv(file_2_name + "_tr.csv")
# print("горизонтальный датафрейм файла_2 -> в csv \n", df_of_file_2_tr.head(), stars)

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
# print("объединенные датафреймы -> csv \n", merged_df, stars)
# merged_df.to_csv("merged_df.csv")

# удалить первую колонку, так как в ней вместо числа содержится текст: hamburger1, hamburger2
merged_df_hamb = merged_df.drop("СЛОВО", axis=1)
# print("удалена колонка содержащая", '->'+hamburger1+'<-', '\n\n',  merged_df_hamb, stars)
# merged_df_hamb.to_csv("merged_df_hamb.csv")

# задать названия индексов
merged_df_hamb_ind = merged_df_hamb.set_axis([hamburger1, hamburger2], axis='index')
# print("названы индексы \n\n",  merged_df_hamb_ind, stars)
# merged_df_hamb_ind.to_csv("merged_df_hamb_ind.csv")

# снова перевернуть (теперь уже объединенный датафрейм)
merged_df_hamb_ind_tr = merged_df_hamb_ind.transpose()
# print("объединенный перевернутый \n\n",  merged_df_hamb_ind_tr, stars)

# сортировать по убыванию
want_sort = False#выбрать здесь
if want_sort is True:
    df_sort_or_not = merged_df_hamb_ind_tr.sort_values(by=[hamburger2], ascending=False)
    # print("сортированный \n\n",  df_sort_or_not, stars)
else:
    df_sort_or_not = merged_df_hamb_ind_tr
df_sort_or_not.to_csv("df_sort_or_not.csv")


# dropna / fillna--------------------------------------------------------
want_drop_nans = input("Удалить nans или заменить на ноль? Введите delete/fill: ")

if want_drop_nans == "delete":
    df_drn_or_filn = df_sort_or_not.dropna(axis=0).astype(int)
    # print("удалены nan \n\n",  df_drn_or_filn, stars)
else:
    df_drn_or_filn = df_sort_or_not.fillna(0).astype(int)  # заменяю nan на ноль
    # print("ЗАМЕНЕНЫ nan \n\n",  df_drn_or_filn, stars)

# select small_df / all_rows--------------------------------------------
select_all_rows = input("Всего строчек: "+str(len(df_drn_or_filn.index))+". Выбрать все строчки таблицы? Введите yes/no: ")

if select_all_rows == "no":
    start_row = int(input("С какой строчки таблицы начать? Введите число: "))
    cactus = int(input("Сколько строчек(=слов) взять? Введите число: "))
    end_row = start_row + cactus
    df_all_or_small = df_drn_or_filn.iloc[start_row:end_row]
else:
    df_all_or_small = df_drn_or_filn

# print("small", '\n\n',  df_all_or_small, stars)


# row totals--------------------------------------------------------------
df_rot = df_all_or_small.copy()
df_rot['row_totals'] = df_all_or_small.sum(axis=1)
# print("row totals \n\n",  df_rot, stars)

# col totals
df_rot_cot = df_rot.copy()
df_rot_cot.loc['col_totals'] = df_rot.sum(axis=0)
# print("col totals \n\n",  df_rot_cot, stars)

# ndarray_expected
amount_of_rows = len(df_rot_cot.index) - 1  # отнимаю строку "col_totals"
amount_of_columns = len(df_rot_cot.columns) - 1  # отнимаю колонку "row_totals"
totaltotal = df_rot_cot.iloc[amount_of_rows][amount_of_columns]  # использую эти переменные, так как индекс на 1 меньше

exp_ndarr = np.outer(df_rot_cot["row_totals"][0:amount_of_rows],
                     df_rot_cot.loc["col_totals"][0:amount_of_columns]) / totaltotal
exp_ndarr_r = exp_ndarr.round(2)

# ndarray_expected ----> df
rows_names_all = df_rot_cot.index
columns_names_all = df_rot_cot.columns

rows_names_red = rows_names_all.drop("col_totals")
columns_names_red = "expected " + columns_names_all.drop("row_totals")

df_exp = pd.DataFrame(exp_ndarr)  # НЕокругл-exp_ndarr / округл-exp_ndarr_r

df_exp.index = rows_names_red
df_exp.columns = columns_names_red
# print("expected df \n\n",  df_exp, stars)

# create observed_df
df_obs = df_rot_cot.iloc[0:amount_of_rows, 0:amount_of_columns]
print("observed df \n\n", df_obs, stars)

print("expected df \n\n", df_exp, stars)

# chi
statistic, pvalue, dof, expected_freq = stats.chi2_contingency(observed=df_obs)
print("statistic", statistic)
print("pvalue", pvalue)
print("dof", dof)
# print("expected_freq\n",expected_freq)
if pvalue <= 0.05:
    print("reject H0, ", "различаются", stars)
else:
    print("мы не обнаружили значимых различий", stars)

from scipy.stats.distributions import chi2

inv = chi2.ppf(0.95, dof)
if statistic > inv:
    print("reject H0,", "H1 = встречаемость слов зависит от файла", stars)
else:
    print("встречаемость слов НЕ зависит от файла. independent.")
    print("not enough evidence to suggest _file_ and _words_ are dependent (at the 5% level of significance)", stars)

#bar plot
if select_all_rows == "no":
    df_obs.plot(kind="bar")
    plt.show()

#line plot
x = df_obs.index
y1 = df_obs[hamburger1]
y2 = df_obs[hamburger2]
plt.plot(x, y1, color="blue", label="obs. distrib. " + hamburger1, alpha=0.3)
plt.plot(x, y2, color="red", label="obs. distrib. " + hamburger2, alpha=0.3)

plt.fill_between(x, y1, color="blue", alpha=0.3)
plt.fill_between(x, y2, color="red", alpha=0.3)

plt.legend()
plt.show()





