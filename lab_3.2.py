import time
import threading
import random


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._file = open("sort_times.txt", "w", encoding="utf-8")
        return cls._instance

    def log(self, message):
        self._file.write(message + "\n")

    def __del__(self):
        self._file.close()


def bubble_sort(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    duration = end_time - start_time
    SingletonLogger().log(f"Bubble Sort: {duration:.6f} seconds")


def shell_sort(arr):
    start_time = time.time()
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    end_time = time.time()
    duration = end_time - start_time
    SingletonLogger().log(f"Shell Sort: {duration:.6f} seconds")


def quick_sort(arr):
    start_time = time.time()

    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    duration = end_time - start_time
    SingletonLogger().log(f"Quick Sort: {duration:.6f} seconds")


if __name__ == "__main__":
    array_size = 1000
    original_array = [random.randint(0, 10000) for _ in range(array_size)]

    array_for_bubble = original_array[:]
    array_for_shell = original_array[:]
    array_for_quick = original_array[:]

    bubble_thread = threading.Thread(target=bubble_sort, args=(array_for_bubble,))
    shell_thread = threading.Thread(target=shell_sort, args=(array_for_shell,))
    quick_thread = threading.Thread(target=quick_sort, args=(array_for_quick,))

    bubble_thread.start()
    shell_thread.start()
    quick_thread.start()

    bubble_thread.join()
    shell_thread.join()
    quick_thread.join()

    print("Sorting completed. Execution times are saved in 'sort_times.txt'")
