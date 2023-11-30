s = input('Введите строку s0 :')
s0 = input('Введите строку s0 :')
count = 0
for i in s:
    if i == s0:
        count = count + 1
    else:
        pass
print(f"Количество вхождений строки {'s0'} в строке {'s'} :" + str(count))