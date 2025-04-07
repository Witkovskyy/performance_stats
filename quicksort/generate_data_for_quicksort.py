import random

def generate_A(num_of_elems):
    data = []
    for i in range(0,num_of_elems+1,2):
        data.append(i)
    for i in range(num_of_elems-1,1,-2):
        data.append(i)
    return data


# print(generate_random(1000))
# print(generate_ascending(100))
# print(generate_A(100))
