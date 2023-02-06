#testing

cat1 = ['abst', 'cyclospor', 'a']

cat2 = ['and', 'methotrexate', 'mtx', 'is']

cat3 = cat1 + cat2
print(cat3)

print(len(cat3))




# два условия, в цикле - как это уместить в одну функцию?
# функц1 - условие1
# функц2 - условие2
# функц3 - цикл с ф1 и ф2




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


