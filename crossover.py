import random

list_a = [random.randint(1,100) for i in range(10)]
list_b = [random.randint(1,100) for i in range(10)]
print list_a, list_b

a = len(list_a) / 2 + 1
b = len(list_b) / 2 + 1
print list_b[:b] + list_a[a:]
print list_a[:a] + list_b[b:]