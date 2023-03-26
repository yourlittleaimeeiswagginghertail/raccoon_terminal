# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   get abstracts   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
with open("павлов22.txt", "r") as text1:
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
oblifrodoc2  = obtained_line_from_doc2
liwiwofrobli = list_with_words_from_obtained_line
liwialtiwo   = list_with_all_titles_words
'''
with open("павлов22.txt", "r") as doc2:
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
#df1.to_csv("result1.csv")
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   summation   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

