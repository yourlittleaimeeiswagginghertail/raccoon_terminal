"""
pandas
print(df1, "\n")
print(df1.head(2), "\n")
print(df1.tail(2), "\n")
print(df1.info(), "\n")


print(cap)

import pandas as pd

df1 = pd.read_csv("spreadsheet_1528 - Sheet1.csv")
print(df1.to_string(), "\n")

cap = df1["numbers"].mean()
df1["numbers"].fillna(cap, inplace = True)

print(df1.to_string(), "\n")

bird = df1.dropna()
print(bird)


import pandas as pd
import numpy as np

car = np.around(np.random.rand(10), 3)
print(car)

grass = np.around(np.random.rand(10), 1)
print(grass)

road = pd.Series(data=car, index=grass)
print(road)
"""

import pandas as pd
original_sheet = pd.read_csv("Запись на подготовку к ассесменту - Лист1.csv")

col_names = list(original_sheet.columns.values)
amount_columns = len(col_names)

renamed_columns = original_sheet.rename(columns={col_names[0]:"peoplenames",
						 col_names[1]:"L1dat_tim",
						 col_names[2]:"L2dat_tim",
						 col_names[3]:"L3dat_tim",
						 col_names[4]:"L4dat_tim",
						 col_names[5]:"-",
						 col_names[6]:"-",
						 col_names[7]:"-",
						 col_names[8]:"-",
						 col_names[9]:"-", })

shcorrected_names1 = renamed_columns.dropna(subset = ["peoplenames"])
sheet_corrected_names2 = shcorrected_names1.drop( index = shcorrected_names1.index[380:] )

col_people_names = sheet_corrected_names2.loc[1: , "peoplenames"]

def short_name (one_name):
	return one_name[0:6] + one_name[10:13]

col_short_names = (col_people_names.apply(short_name)).to_string()

sheet_corrected_names2["peoplenames"] = col_short_names
print(sheet_corrected_names2.to_string())




#print(renamed_columns.to_string())
"""

#print(building.info(), "\n")
buil_1 = building

buil2 = buil_1.drop("Применяет стандарты и методики при оформлении программного кода", axis =1)
buil3 = buil2.drop("Применяет системы контроля версий", axis =1)
buil4 = buil3.drop("Применяет СУБД", axis =1)
buil5 = buil4.drop("Unnamed: 5", axis =1)
buil6 = buil5.drop("Unnamed: 6", axis =1)
buil7 = buil6.drop("Unnamed: 7", axis =1)
buil8 = buil7.drop("Unnamed: 8", axis =1)
#print(buil8.info())
active_students = buil8.dropna()

#print(active_students.to_string())

#only_names = active_students.drop([382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393], axis =0)
for repeat in range (37):
  active_students = active_students.drop(active_students.index[-1])
#удалить верхнуюю строчку с примером
active_students = active_students.drop(active_students.index[0])
#useless_indexes = active_students.iloc[377:]
only_names = active_students
#print(only_names.to_string())
#print(only_names.tail(10))
only_names = only_names.rename(columns={"Unnamed: 0":"names", "Применяет языки программирования для решения профессиональных задач":"L_1_date_time"})

#print(only_names.to_string())

#print(only_names.info())


only_names = only_names.sort_values(["L_1_date_time"])
print(only_names.to_string())

#result = only_names.to_csv("result.csv")
only_names.to_csv("result.csv")
from google.colab import files
files.download("result.csv")

"""
