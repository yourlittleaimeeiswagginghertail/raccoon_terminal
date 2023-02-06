with open("павлов22.txt", "r") as text1:
    separator1 = "██████████████████████" #"https://emojicombos.com/"
    
    row = "start"
    this_row_belongs_to_abstract = False
    art_count = 1
    print(separator1, "article № " + str(art_count) + ": " + separator1)
    all_words1 = []
    while row != "":
        row = text1.readline()
        row_cat = row.split(" ")
        if row_cat[0] ==   "Abstract:":
            this_row_belongs_to_abstract = True
        elif row_cat[0] == "Keywords:":
            this_row_belongs_to_abstract = False
        elif row ==        "\n": 
            this_row_belongs_to_abstract = False
            art_count += 1
            print(separator1, "article № " + str(art_count) + ": " + separator1)
        else:
            condition1 = "else1"


        if this_row_belongs_to_abstract is True:
            #print(row_cat)
            all_words1 = all_words1 + row_cat
        else:
            condition2 = "else2"



print("\n\n всего слов во всех абстрактах:", len(all_words1), "вот они:")
#print(all_words1)

'''
small_part1 = all_words1[0:30]
all_words1 = small_part1
#print(all_words1)
'''


from collections import Counter
words_repeat1 = dict(Counter(all_words1))
print(words_repeat1)

import pandas as pd
df1 = pd.DataFrame.from_dict(words_repeat1, orient = 'index')
print(df1)
#df1.to_csv("result1.csv")

'''
    row_names = 1
    row_title = 2
    row_abstract = 10
    row_keywords = 11
    row_blank = 12 #row == "\n"
    separator2 = "◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤"
    print(*row_cat, sep=" ")
'''
