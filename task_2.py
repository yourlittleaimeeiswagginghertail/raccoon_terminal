#for saving code
quote = "If Socialism can only be realized when the intellectual development of all the people permits it, then we shall not see Socialism for at least five hundred years"

words = quote.split(" ")

#print(words)

selected = []

for onewo in words:
	#print(onewo)
	lecount = 0
	for letter in onewo:
		#print(letter)
		selected.append(letter)
		lecount += 1
		if lecount == 2:
			break
		else:
			nothing =  "nothing"

#print(selected)
result =  "".join(selected)
print(result, "\n")
print(quote)
