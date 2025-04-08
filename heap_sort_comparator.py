import time
from generate_data import generate_random, generate_ascending, generate_descending, generate_V



#Data range
starting_num = 1000
finish_num = 25000
step = 5000

def heapify(A, i, heapsize):
    l = 2 * i
    r = 2 * i + 1  
    largest = i

    if l <= heapsize and A[l] > A[largest]:
        largest = l

    if r <= heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heapsize)

def build_heap(A):
    heapsize = len(A) - 1 
    for i in range(heapsize // 2, 0, -1): 
        heapify(A, i, heapsize)

def heap_sort(A):
    A = [None] + A 
    build_heap(A)
    heapsize = len(A) - 1

    for i in range(heapsize, 1, -1):
        A[1], A[i] = A[i], A[1]
        heapsize -= 1 
        heapify(A, 1, heapsize)

    return A[1:]  # Cut `None`


# n = int(input("Podaj liczbe elementow"))

with open("heap.txt", "w",encoding="utf-8") as f:
    f.write("Random,Ascending,Descending,V-shaped")
    f.write("\n")
    f.close()

for i in range(starting_num, finish_num, step):
    n = i


    times_random = []
    data_random = generate_random(n)
    for i in range(0, 10):
        A = data_random.copy()
        start = time.perf_counter_ns()
        A = heap_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_random.append(elapsed)
    # print(times)
    sum_random = 0
    for item in times_random:
        sum_random +=item
    avg_random = sum_random/10
    avg_random = round(avg_random)

    times_asc = []
    data_asc = generate_ascending(n)
    for i in range(0, 10):
        A = data_asc.copy()
        start = time.perf_counter_ns()
        A = heap_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_asc.append(elapsed)
    # print(times2)
    sum_asc = 0
    for item in times_asc:
        sum_asc +=item
    avg_asc = sum_asc/10
    avg_asc = round(avg_asc)

    times_desc = []
    data_desc = generate_descending(n)
    for i in range(0, 10):
        A = data_desc.copy()
        start = time.perf_counter_ns()
        A = heap_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_desc.append(elapsed)
    # print(times_desc)

    sum_desc = 0
    for item in times_desc:
        sum_desc +=item
    avg_desc = sum_desc/10
    avg_desc = round(avg_desc)

    times_v = []
    data4 = generate_V(n)
    for i in range(0, 10):
        A = data4.copy()
        start = time.perf_counter_ns()
        A = heap_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_v.append(elapsed)
    # print(times_v)
    sum_v = 0
    for item in times_v:
        sum_v +=item
    sum_v = sum_v/10
    sum_v = round(sum_v)
 
    with open("heap.txt", "a") as f:
        f.write(f"{avg_random},{avg_asc},{avg_desc},{sum_v}\n")
        f.close()