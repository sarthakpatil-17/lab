# Binary Search in Python using User Input

arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))

target = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index", mid)
        found = True
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found")
