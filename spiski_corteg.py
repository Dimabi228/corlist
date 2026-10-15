# МНОЖЕСТВА 

# Задание 1
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
my_set = set(numbers)
print(f"Множество: {my_set}")
print(f"Количество элементов: {len(my_set)}")

# Задание 2
my_set = {10, 20, 30}
print(f"Исходное множество: {my_set}")
my_set.add(40)
print(f"После добавления 40: {my_set}")
my_set.remove(20)
print(f"После удаления 20: {my_set}")

# Задание 3
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
print(f"Объединение: {set1 | set2}")

# Задание 4
print(f"Пересечение: {set1 & set2}")

# Задание 5
print(f"В первом, но нет во втором: {set1 - set2}")
print(f"Во втором, но нет в первом: {set2 - set1}")

# Задание 6
print(f"Входят ровно в одно: {set1 ^ set2}")

# Задание 7
my_set = {1, 2, 3, 4, 5}
x = 3
print(f"Множество: {my_set}, x = {x}")
if x in my_set:
    print(f"{x} есть в множестве")
else:
    print(f"{x} нет в множестве")

# Задание 8
set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}
print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
if set1.issubset(set2):
    print("Первое множество является подмножеством второго")
else:
    print("Первое множество НЕ является подмножеством второго")

# Задание 9
text = "hello world"
unique_chars = set(text)
print(f"Строка: '{text}'")
print(f"Различные символы: {unique_chars}")
print(f"Количество различных символов: {len(unique_chars)}")

# Задание 10
list1 = [1, 2, 3, 4, 5, 5, 6]
list2 = [4, 5, 5, 6, 7, 8, 9]
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
common = sorted(set(list1) & set(list2))
print(f"Общие элементы без повторов: {common}")


#КОРТЕЖИ 

# Задание 1
t = (10, 20, 30, 40, 50)
print(f"Кортеж: {t}")
print(f"Первый: {t[0]}")
print(f"Последний: {t[-1]}")
print(f"Средний: {t[len(t) // 2]}")

# Задание 2
t = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"Кортеж: {t}")
print(f"Первые два: {t[:2]}")
print(f"Последние два: {t[-2:]}")
print(f"В обратном порядке: {t[::-1]}")

# Задание 3
t = (5, 2, 8, 1, 9, 3)
print(f"Кортеж: {t}")
print(f"Длина: {len(t)}")
print(f"Сумма: {sum(t)}")
print(f"Минимум: {min(t)}")
print(f"Максимум: {max(t)}")

# Задание 4
t = (1, 2, 3, 2, 4, 2, 5)
x = 2
print(f"Кортеж: {t}, x = {x}")
if x in t:
    print(f"{x} есть в кортеже")
    print(f"Встречается {t.count(x)} раз")
    print(f"Индекс первого вхождения: {t.index(x)}")
else:
    print(f"{x} нет в кортеже")

# Задание 5
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(f"Кортеж 1: {t1}")
print(f"Кортеж 2: {t2}")
print(f"Объединённый кортеж: {t1 + t2}")

# Задание 6
t = (42,)
print(f"Кортеж: {t}")
print(f"Тип: {type(t)}")
not_tuple = (42)
print(f"Без запятой: {not_tuple}, тип: {type(not_tuple)}")

# Задание 7
person = ("Анастасия", 25, "Москва")
name, age, city = person
print(f"Кортеж: {person}")
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Город: {city}")

# Задание 8
a = 5
b = 10
print(f"До: a = {a}, b = {b}")
a, b = b, a
print(f"После: a = {a}, b = {b}")

# Задание 9
t = (10, 20, 30, 40, 50)
new_t = t[:1] + (99,) + t[2:]
print(f"Исходный: {t}")
print(f"Новый: {new_t}")

# Задание 10
t = (5, 3, 5, 1, 3, 2, 1, 4)
unique_sorted = tuple(sorted(set(t)))
print(f"Исходный: {t}")
print(f"Без повторов, отсортированный: {unique_sorted}")