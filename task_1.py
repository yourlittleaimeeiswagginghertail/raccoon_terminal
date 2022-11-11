def trying_1(masu_1):
    try:
        return float(input("введи " + str(masu_1 + 1) + "-ое " + "число: "))
    except ValueError:
        return "значением функции является сейчас этот текст"

numbers = []
for masu_1 in range(100):    
    catched_number = trying_1(masu_1)
    if type(catched_number) != float:
        print(catched_number)
    else:
        if catched_number == 0:
            break
        else:
            numbers.append(catched_number)




    
print("числа которые ты ввел:", numbers)
print("их сумма:", sum(numbers))

counter = 0
for element in numbers:
    counter += 1
    #print(element, counter)

print("их среднее арифм:", sum(numbers)/counter)
