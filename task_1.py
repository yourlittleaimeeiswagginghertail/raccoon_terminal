










import numpy as np
import pandas as pd

available_letters = "абвг"
amount_of_av_let = len(available_letters)
cat_of_letters = list(available_letters)
print(" ваши буквы:", *cat_of_letters, sep=" ")
#####################
message = "\n введите нужную длину слова \n из расставленных рандомно букв: "
how_much_indexes = int(input(message))
#####################
for repeat in range(1):
    indexes_for_letters = np.random.randint(0, amount_of_av_let, how_much_indexes)

    letters_from_indexes = np.take(cat_of_letters, indexes_for_letters)
    strange_word = "".join(letters_from_indexes)
    print("\n слово из букв:", strange_word, "\n")


ser = pd.Series(letters_from_indexes)
#print(ser, "\n")

print(ser.value_counts(normalize=False), "\n")
print(ser.value_counts(normalize=True ))
