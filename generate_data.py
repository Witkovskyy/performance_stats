import random

def generate_random(num_of_elems):
    data = []
    for i in range(0, num_of_elems):
        data.append(random.randint(1,10000))
    return data

def generate_ascending(num_of_elems):
    data = []
    for i in range(0, num_of_elems):
        data.append(i)
    return data

def generate_descending(num_of_elems):
    data = []
    for i in range(num_of_elems,0, -1):
        data.append(i)
    return data

def generate_V(num_of_elems):
    data = []
    for i in range(num_of_elems,1,-2):
        data.append(i)
    for i in range(1,num_of_elems,2):
        data.append(i)
    return data


# print(generate_random(1000))
# print(generate_ascending(100))
# print(generate_V(100))
