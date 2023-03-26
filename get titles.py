#потом переименовать все переменные, чтобы они не путались с файлом getabstracts

with open("павлов22.txt", "r") as text1:    
    row = "start"
    this_row_is_title = False
    all_titles_words = []
#для первой статьи - взять вторую строку
    row = text1.readline()#первая строчка
    row = text1.readline()#вторая строчка
    #print(row)
    row_cat = row.split(" ")
    all_titles_words = all_titles_words + row_cat#сразу сохр в общ список 
    #print(all_titles_words)
#для последующих статей - цикл
#between articles "\n"
#title - second row after "\n"
    while row != "": #это до конца текстового файла
        row = text1.readline()
        if row == "\n":#это значит что я на строчке-разрыве между статьями
            row = text1.readline()#отсчитываю первую строчку после разрыва
            row = text1.readline()#отсчитываю вторую строчку после разрыва
            #print(row)
            row_cat = row.split(" ")
            all_titles_words = all_titles_words + row_cat #сохраняю в общий список
        else:
            condition1 = "else1"

print(all_titles_words)

# ВНЕДРИТЬ В ФАЙЛ БЕРУЩИЙ АБСТРАКТЫ = просто приплюсовать списки слов


'''
row = obtained_line_from_text1 = oblifrotext1
text1 = doc2
all_titles_words = list_with_all_titles_words = liwialtiwo
row_cat = list_with_words_from_oblifrotext1 = liwiwofrobli

this_row_is_title = oblifrotext1_is_title
'''
