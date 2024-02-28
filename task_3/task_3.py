import timeit
from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search

# Зчитуємо вміст файлів
with open("task_3/article1.txt", "r") as file:
    article1 = file.read()

with open("task_3/article2.txt", "r") as file:
    article2 = file.read()

# Тестові підрядки (один, що дійсно існує в тексті, та інший - вигаданий)
existing_substring1 = "послідовність точно визначених дій"
non_existing_substring1 = "велосипед та подорож"

existing_substring2 = "додавання і вилучення ребер"
non_existing_substring2 = "велосипед та подорож"

# Вимірюємо час для алгоритмів на першому тексті
print("Алгоритм Кнута-Морріса-Пратта для першого тексту (існуючий підрядок):", timeit.timeit(lambda: kmp_search(article1, existing_substring1), number=1000))
print("Алгоритм Боєра-Мура для першого тексту (існуючий підрядок):", timeit.timeit(lambda: boyer_moore_search(article1, existing_substring1), number=1000))
print("Алгоритм Рабіна-Карпа для першого тексту (існуючий підрядок):", timeit.timeit(lambda: rabin_karp_search(article1, existing_substring1), number=1000))

print("Алгоритм Кнута-Морріса-Пратта для першого тексту (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(article1, non_existing_substring1), number=1000))
print("Алгоритм Боєра-Мура для першого тексту (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(article1, non_existing_substring1), number=1000))
print("Алгоритм Рабіна-Карпа для першого тексту (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(article1, non_existing_substring1), number=1000))

# Вимірюємо час для алгоритмів на другому тексті
print("Алгоритм Кнута-Морріса-Пратта для другого тексту (існуючий підрядок):", timeit.timeit(lambda: kmp_search(article2, existing_substring2), number=1000))
print("Алгоритм Боєра-Мура для другого тексту (існуючий підрядок):", timeit.timeit(lambda: boyer_moore_search(article2, existing_substring2), number=1000))
print("Алгоритм Рабіна-Карпа для другого тексту (існуючий підрядок):", timeit.timeit(lambda: rabin_karp_search(article2, existing_substring2), number=1000))

print("Алгоритм Кнута-Морріса-Пратта для другого тексту (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(article2, non_existing_substring2), number=1000))
print("Алгоритм Боєра-Мура для другого тексту (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(article2, non_existing_substring2), number=1000))
print("Алгоритм Рабіна-Карпа для другого тексту (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(article2, non_existing_substring2), number=1000))
