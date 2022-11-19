import numpy as np

#создать array
bath = np.arange(51)

#c десятого индекса, до последнего, шаг два
birthday = bath[10: :2]
print(birthday)

#в обратном порядке
sympathy = np.flip(birthday, 0)
print(sympathy)
