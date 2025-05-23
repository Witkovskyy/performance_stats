import time
from generate_data import generate_random, generate_ascending, generate_descending, generate_V



#Data range
starting_num = 5000
finish_num = 50000
step = 5000


def merge_sort_main(A):
    B = [0] * len(A)  
    merge_sort(A, 0, len(A) - 1, B)
    return A

def merge_sort(A, l, r, B):
    if l < r:
        m = (l + r) // 2 
        merge_sort(A, l, m, B)  
        merge_sort(A, m + 1, r, B)
        merge(A, l, m, r, B)  

def merge(A, l, m, r, B):
    i = l  
    j = m + 1  

    for k in range(l, r + 1):
        if (i <= m and (j > r or A[i] <= A[j])):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

    for k in range(l, r + 1):
        A[k] = B[k]


# n = int(input("Podaj liczbe elementow"))

with open("merge.txt", "w",encoding="utf-8") as f:
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
        A = merge_sort_main(A)
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
        A = merge_sort_main(A)
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
        A = merge_sort_main(A)
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
        A = merge_sort_main(A)
        end = time.perf_counter_ns()
        elapsed = (end - start) / 1_000_000 
        times_v.append(elapsed)
    # print(times4)
    sum_v = 0
    for item in times_v:
        sum_v +=item
    sum_v = sum_v/10
    sum_v = round(sum_v)


    with open("merge.txt", "a") as f:
        f.write(f"{avg_random},{avg_asc},{avg_desc},{sum_v}\n")
        f.close()