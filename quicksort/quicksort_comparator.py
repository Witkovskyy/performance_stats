from generate_data_for_quicksort import generate_A
import time
import random
import sys

sys.setrecursionlimit(10000)

#Data range
starting_num = 1000
finish_num = 50000
step = 5000

def quicksort_main(A, pivot_picker):
    quicksort(A, 0, len(A) - 1, pivot_picker)  
    return A

def quicksort(A, p, r, pivot_picker):
    if p < r:
        q = partition(A, p, r, pivot_picker)  
        quicksort(A, p, q - 1, pivot_picker)
        quicksort(A, q + 1, r, pivot_picker) 

def partition(A, p, r, pivot_picker):
    match pivot_picker:
        case 0:
            x = A[r] # Pivot - max right
        case 1:
            x = A[(p + r) // 2]  # Pivot – middle
        case 2:
            x = A[random.randint(p, r)] #Pivot - random

    i = p - 1
    j = r + 1
    
    while True:
        while True:
            j -= 1
            if A[j] <= x:  
                break
        
        while True:
            i += 1
            if A[i] >= x:  
                break
        
        if i < j:
            A[i], A[j] = A[j], A[i]  
        else:
            return j  


with open("quick.txt", "w",encoding="utf-8") as f:
    f.write("Right, Middle, Random")
    f.write("\n")
    f.close()

for i in range(starting_num, finish_num, step):
    n = i
    pivot_picker = 0
    data = generate_A(n)

    times_right = []
    for i in range(0, 10):
        A = data.copy()
        start = time.perf_counter_ns()
        A = quicksort_main(A, pivot_picker)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_right.append(elapsed)
    sum_right = 0
    for item in times_right:
        sum_right +=item
    avg_right = sum_right/10
    avg_right = round(avg_right)

    pivot_picker += 1
    times_middle = []
    for i in range(0, 10):
        A = data.copy()
        start = time.perf_counter_ns()
        A = quicksort_main(A, pivot_picker)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_middle.append(elapsed)
    sum_middle = 0
    for item in times_middle:
        sum_middle +=item
    avg_middle = sum_middle/10
    avg_middle = round(avg_middle)

    pivot_picker += 1
    times_random = []
    for i in range(0, 10):
        A = data.copy()
        start = time.perf_counter_ns()
        A = quicksort_main(A, pivot_picker)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_random.append(elapsed)
    sum_random = 0
    for item in times_random:
        sum_random +=item
    avg_random = sum_random/10
    avg_random = round(avg_random)



    with open("quick.txt", "a") as f:
        f.write(f"{avg_right},{avg_middle},{avg_random}\n")
        f.close()