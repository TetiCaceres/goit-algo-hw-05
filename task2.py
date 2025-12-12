def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iteration = 0
    upper_bound = None
    EPS = 1e-9
 
    while low <= high:
        iteration += 1
 
        mid = (high + low) // 2
 
        
        if abs(arr[mid] - x) < EPS:
            return (iteration, arr[mid])
        
        if arr[mid] < x - EPS:
            low = mid + 1

        else:
            upper_bound = arr[mid]
            high = mid - 1

    return (iteration, upper_bound)
 
    # якщо елемент не знайдений
    return -1

arr = [0.1, 0.2, 0.5, 1.0, 1.5, 2.3, 3.14, 4.7, 6.0, 8.3]
tests = [0.05, 0.2, 0.7, 1.5, 3.0, 6.0, 8.3, 9.0]

for x in tests:
    iterations, upper_bound = binary_search(arr, x)
    print(f"x = {x:4} → iterations = {iterations}, upper bound = {upper_bound}")
