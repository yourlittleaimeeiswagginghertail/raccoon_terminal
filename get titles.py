#потом переименовать все переменные, чтобы они не путались с файлом getabstracts

with open("павлов22.txt", "r") as text1:
    separator1 = "██████████████████████" #"https://emojicombos.com/"
    
    row = "start"
    this_row_is_title = False
    art_count = 1
    print(separator1, "article № " + str(art_count) + ": " + separator1)
    all_titles_words = []

#для первой статьи - взять вторую строку
    row = text1.readline()#первая строчка
    row = text1.readline()#вторая строчка
    #print(row)
    row_cat = row.split(" ")
    all_titles_words = all_titles_words + row_cat#сразу сохр в общ список 
    #print(all_titles_words)

#для последующих статей - написать цикл
#between articles "\n"
#title - second row after "\n"


    while row != "": #это до конца текстового файла
        row = text1.readline()
        if row == "\n":#это значит что я на строчке-разрыве между статьями
            row = text1.readline()#отсчитываю первую строчку после разрыва
            row = text1.readline()#отсчитываю вторую строчку после разрыва
            print(row)
        else:
            condition1 = "else1"

#ТЕПЕРЬ СОХРАНИТЬ ВСЕ НАЗВАНИЯ В СПИСОК СЛОВ И ВНЕДРИТЬ В ФАЙЛ БЕРУЩИЙ АБСТРАКТЫ



