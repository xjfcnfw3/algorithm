t = int(input())

def find(people):
    if people not in network:
        network[people] = people
        network_number[people] = 1
    if network[people] != people:
        network[people] = find(network[people])
    return network[people]

def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root == b_root:
        print(network_number[a_root])
        return
    elif a_root < b_root:
        network[b_root] = a_root
        network_number[a_root] += network_number[b_root]
        print(network_number[a_root])
    else:
        network[a_root] = b_root
        network_number[b_root] += network_number[a_root]
        print(network_number[b_root])

for _ in range(t):
    n = int(input())
    network = dict()
    network_number = dict()
    for _ in range(n):
        a, b = input().split()
        union(a, b)