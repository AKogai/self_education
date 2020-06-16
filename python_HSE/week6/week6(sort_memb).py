# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и
# выведите его, отсортировав по фамилии в
# лексикографическом порядке. При выводе указываете
# фамилию, имя участника и его балл. Используйте для
# ввода и вывода файлы input.txt и output.txt
# с указанием кодировки utf8. Например, для чтения
# откройте файл с помощью open('input.txt', 'r',
# encoding='utf8').


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
people_list = []
i = 0
for line in lines:
    people_list.append(line.split())
people_list.sort()
for i in people_list:
    print(i[0], i[1], i[3], file=outFile)
inFile.close()
outFile.close()
