import pandas as pd
original_sheet = pd.read_csv("Запись на подготовку к ассесменту - Лист1.csv")

col_titles = list(original_sheet.columns.values)
renamed_columns_titles = original_sheet.rename(columns={
                                                 col_titles[0]:"peoplenames",
						 col_titles[1]:"L1dat_tim",
						 col_titles[2]:"L2dat_tim",
						 col_titles[3]:"L3dat_tim",
						 col_titles[4]:"L4dat_tim",
						 col_titles[5]:"5-",
						 col_titles[6]:"6-",
						 col_titles[7]:"7-",
						 col_titles[8]:"8-",
						 col_titles[9]:"9-", })
new_col_titles = list(renamed_columns_titles.columns.values)

shcorrected_names1 = renamed_columns_titles.dropna(subset = ["peoplenames"])
sheet_corrected_names2 = shcorrected_names1.drop( index = shcorrected_names1.index[380:] )


col_people_names = sheet_corrected_names2.loc[0: , "peoplenames"]
def short_name (one_name):
	return one_name[0:20]
col_short_names = col_people_names.apply(short_name)
sheet_corrected_names2["peoplenames"] = col_short_names


required_columns = sheet_corrected_names2.drop([ #new_col_titles[0],
                                                 new_col_titles[1],
                                                 #new_col_titles[2],
                                                 new_col_titles[3],
                                                 new_col_titles[4],
                                                 new_col_titles[5],
                                                 new_col_titles[6],
                                                 new_col_titles[7],
                                                 new_col_titles[8],
                                                 new_col_titles[9],
                                                 ] , axis=1)



active_students = required_columns.dropna()
print(active_students.to_string())
#active_students.to_csv("results.csv")
