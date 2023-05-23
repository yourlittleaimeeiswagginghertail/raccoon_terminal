import pandas as pd

with open("transposed.csv", "r+") as csvtext1:
    csv_str1 = csvtext1.read()

    stop = csv_str1.index("СЛОВО")
    for masu1 in range(stop):
        symbol = csv_str1[0]
        csv_str1 = csv_str1.replace(symbol, "", 1)
    #print("\n", csv_str1)

    csvtext1.close()



new_file = open("new_file.csv",'w')
new_file.write(csv_str1)
new_file.close()

#print("\n", csv_str1)


df = pd.read_csv("new_file.csv")
print(df.head())


'''
    end = csv_str1.index("СЛОВО")

    for repl_ind in range(end):
        #first = csvstr1[0]
        csv_str1[repl_ind] = ""
        print(csv_str1)
        #csvtext1.write(csv_str2)

        
    #print(start, end)
'''
