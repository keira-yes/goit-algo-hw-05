def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # Якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # Якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # Інакше x присутній на позиції
        else:
            return iterations, arr[mid]
 
     # якщо елемент не знайдений, повертаємо верхню межу
    if low > len(arr) - 1:
        return iterations, arr[-1]
    elif high < 0:
        return iterations, arr[0]
    else:
        return iterations, arr[low]

# Тестуємо:
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
print(binary_search(arr, 2.5))
print(binary_search(arr, 3.5))
print(binary_search(arr, 6.0))