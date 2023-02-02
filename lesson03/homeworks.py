# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

def homework1():
    lst = input("Введите массив:").split(',')
    search = input("Введите искомый символ:")
    print(len([item for item in lst if item == search]))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


def homework2():
    lst = list(map(int, input("Введите массив:").split(',')))
    search = int(input("Введите число для поиска ближайшего по величине:"))
    search2 = lst[0]
    for item in lst:
        if (abs(search-item) < abs(search-search2)):
            search2 = item
    print(search2)


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12
def getGrade(gradeDict, ch):
    nop = 0
    for item in gradeDict.items():
        if ch in [lstr.strip() for lstr in item[1].split(',')]:
            nop += int(item[0])
    return nop


def homework3():
    gradeDictEn = {1: "A, E, I, O, U, L, N, S, T, R", 2: "D, G", 3: "B, C,", 4: "F, H, V, W, Y ",
                   5: "K", 8: "J, X", 10: "Q, Z"}
    gradeDictRu = {1: "А, В, Е, И, Н, О, Р, С, Т", 2: "Д, К, Л, М, П, У", 3: "Б, Г, Ё, Ь, Я", 4: "Й, Ы",
                   5: "Ж, З, Х, Ц, Ч", 8: "Ш, Э, Ю", 0: "Ф, Щ, Ъ"}
    pstr = input("Введите строку:").upper()
    nop = 0
    for ch in pstr:
        nop += getGrade(gradeDictEn, ch)+getGrade(gradeDictRu, ch)
    print(nop)


homework3()