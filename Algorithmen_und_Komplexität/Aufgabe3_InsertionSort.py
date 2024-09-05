import random
import time
#importe um die Zeit zu visualisieren
import matplotlib.pyplot as plt
import numpy as np

def generate_arrays():
    array_lengths = [100, 200, 300,400,500,600,700,800,900,1000,2000,4000,8000,16000]
    arrays = []

    for length in array_lengths:
        array = [random.randint(1, 100) for _ in range(length)]
        arrays.append(array)

    return arrays

arrays = generate_arrays()



def insertion_sort():
    beforesorted = time.time()
    arrays = generate_arrays()
    sorted_arrays = []

    for array in arrays:
        sorted_array = array.copy()
        for i in range(1, len(sorted_array)):
            key = sorted_array[i]
            j = i - 1
            while j >= 0 and key < sorted_array[j]:
                sorted_array[j + 1] = sorted_array[j]
                j -= 1
            sorted_array[j + 1] = key
        sorted_arrays.append(sorted_array)
        aftersorted = time.time()
        print(aftersorted - beforesorted)
    return sorted_arrays

sorted_arrays = insertion_sort()

t = np.linspace(time.time)


