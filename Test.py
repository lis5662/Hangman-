age = int(input('Введите ваш возраст: '))   # простой вариант преобразования строки (str) в целое число (int)
#int_age = int(age)                         # второй вариант более сложный и занимает больше строк
if age < 28:
    print('Поздравляю, Вы - Молодой козлик!')
else:
    print('Увы, но вы - Старикашка!')

# Цикл while 
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print('С Новым годом!')    

# continue for
for i in range(1, 7):
    if i == 3:
        continue
    print(i)

    
#continue while
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


#Задача

list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
added = []
for i in list_1:
    for j in list_2:
        added.append(i * j)
print(added)

    
