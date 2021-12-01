sentence = input("Введите текст: ")
check = 0
print("Символ\tКоличество\tЧастота\t")
print("------\t----------\t-------\t")
for each in list(sentence):
    for each2 in list(sentence):
        if each == each2:
            check = check+1
    procent = check/len(sentence)*100
    print(each,'\t', check,'\t', procent,'\t')
    check = 0