import time
from generate_data import generate_random, generate_ascending, generate_descending, generate_V



def selection_sort(A):
    n = len(A)
    for j in range(n - 1, 0, -1): 
        max_idx = j
        for i in range(j - 1, -1, -1): 
            if A[i] > A[max_idx]: 
                max_idx = i
        A[j], A[max_idx] = A[max_idx], A[j]
    return A


with open("selection.txt", "w",encoding="utf-8") as f:
    f.write("Random,Ascending,Descending,V-shaped")
    f.write("\n")
    f.close()

# n = int(input("Podaj liczbe elementow"))

for i in range(400,7000,100):
    n = i

    times_random = []
    data_random = generate_random(n)
    for i in range(0, 10):
        A = data_random.copy()
        start = time.perf_counter_ns()
        A = selection_sort(A)
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
        A = selection_sort(A)
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
        A = selection_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_desc.append(elapsed)
    # print(times3)
    sum_desc = 0
    for item in times_desc:
        sum_desc +=item
    avg_desc = sum_desc/10
    avg_desc = round(avg_desc)

    times_v = []
    data_v = generate_V(n)
    for i in range(0, 10):
        A = data_v.copy()
        start = time.perf_counter_ns()
        A = selection_sort(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_v.append(elapsed)
    # print(times4)
    sum_v = 0
    for item in times_v:
        sum_v +=item
    sum_v = sum_v/10
    sum_v = round(sum_v)

    with open("selection.txt", "a") as f:
        f.write(f"{avg_random},{avg_asc},{avg_desc},{sum_v}\n")
        f.close()
