# data = [[int(y) for y in x] for x in (line.split() for line in open("test.txt", "r").readlines())]
data = [[int(y) for y in x] for x in (line.split() for line in open("day9.txt", "r").readlines())]

print(data)

def is_only_zeros(x):
    for i in x:
        if i!=0:
            return False
    return True

def calculate_next(d):
    ns = []
    for i in range(len(d) - 1):
        ns.append(d[i + 1] - d[i])
    return ns

new_data=[]
for d in data:
    new_sequence = [d]
    # print(calculate_next(d))
    while not is_only_zeros(d):
        d=calculate_next(d)
        new_sequence.append(d)
    new_data.append(new_sequence)
# print(new_data)

sum_placeholder=0
for d in new_data:
    placeholder = 0
    for i in range(len(d)-1, -1, -1):
        placeholder+=d[i][-1]
    sum_placeholder+=placeholder
print(sum_placeholder)

sum_placeholder=0
for d in new_data:
    placeholder = 0
    for i in range(len(d)-1, -1, -1):
        placeholder=d[i][0]-placeholder
    sum_placeholder+=placeholder
print(sum_placeholder)