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
print(liwialtiwo)

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   get titles   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑



