numbers = []


for repeat in range(100):

    
    try:
        num_1 = float(input("введи число: "))
    except ValueError:
        print("\n это не число")
        num_1 = "нет значения"

        
    if num_1 == 0:
        break
    else:
        numbers.append(num_1)




    
print("числа которые ты ввел:", numbers)
print("их сумма:", sum(numbers))

counter = 0
for element in numbers:
    counter += 1
    #print(element, counter)

print("их среднее арифм:", sum(numbers)/counter)
