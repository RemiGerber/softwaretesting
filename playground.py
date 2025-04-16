def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def max_of_two(a, b):
    return a if a > b else b

def min_of_two(a, b):
    return a if a < b else b

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    # Beispiel-Test für die add() Funktion
    if add(1,2) == 3 and add(1,-1) == 0 and add(0,0) == 0 and add("test", "test2") == "testtest2":
        print("Add Test bestanden!")
    if subtract(2, 1) == 1 and subtract(2, 2) == 0 and subtract(2, 3) == -1:
        print("passed subtraction test")
    if multiply(3,2) == 6 and multiply(3,0) == 0 and multiply(0,3) == 0:
        print("passed multiplication test")
    if divide(4,2) == 2 and divide(4,0) == None and divide(0,4) == 0:
        print("passed division test")
    if is_even(4) == True and is_even(3) == False and is_even(0) == True:
        print("passed even test")
    if is_odd(3) == True and is_odd(4) == False and is_odd(0) == False:
        print("passed odd test")
    if max_of_two(3,4) == 4 and max_of_two(4,3) == 4 and max_of_two(3,3) == 3:
        print("passed max test")
    if min_of_two(3,4) == 3 and min_of_two(4,3) == 3 and min_of_two(3,3) == 3:
        print("passed min test")
    if reverse_string("hello") == "olleh":
        print("passed reverse test")
    if count_vowels("hello") == 2 and count_vowels("aeiou") == 5 and count_vowels("bcdfghjklmnpqrstvwxyz") == 0 and count_vowels("") == 0:
        print("passed vowel count test")
    if factorial(5) == 120 and factorial(0) == 1 and factorial(-1) == None:
        print("passed factorial test")
    if is_palindrome("kayak") == True and is_palindrome("hello") == False and is_palindrome("a") == True and is_palindrome(11) == True:
        print("passed palindrome test") 
    if binary_search([1, 2, 3, 4, 5], 2) == 1:
        print("passed binary search test")