yourinput = input("Твоя строка: ")
count = 0
vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
for letter in yourinput :
    if letter in vowels : 
        count += 1
print("Количество гласных равно:", count)

count1 = 0
vowels1 = set(" ")
for letter in yourinput :
    if letter in vowels1 :
        count1 += 1
print("Количество пробелов равно:", count1)

count2 = 0
vowels2 = set("1234567890")
for letter in yourinput :
    if letter in vowels2 :
        count2 += 1
print("Количество цифр равно:", count2)

# Надо решить тут по-другому как по методичке, там это есть. Это Подсчёт символов