data = open("day8.txt", "r").readlines()
# data = open("test.txt", "r").readlines()

# print(data)
LR_instructions = data[0].strip()
map = []
for i in range(2, len(data)):
    node = data[i].strip()
    node = node.replace(' = ',' ')
    node = node.replace('(','')
    node = node.replace(',','')
    node = node.replace(')','')
    map.append(node.split())
print(map)
print(LR_instructions)

def get_node_by_name(name):
    for node in map:
        if node[0]==name:
            return node

def part1():
    node='AAA'
    step=0
    i=0
    while node!='ZZZ':
        if LR_instructions[i]=='R':
            node=get_node_by_name(node)[2]
        else:
            node=get_node_by_name(node)[1]
        step+=1
        i+=1
        if i>=len(LR_instructions):
            i=0
    print(step)


nodes = []
for node in map:
    if node[0][-1]=='A':
        nodes.append(node[0])
print(nodes)
step=0
i=0
all_Z=False
while not all_Z:
    new_nodes = []
    for node in nodes:
        print(node)
        if LR_instructions[i] == 'R':
            node = get_node_by_name(node)[2]
        else:
            node = get_node_by_name(node)[1]
        new_nodes.append(node)
        print(new_nodes)
        step += 1
        i += 1
        if i >= len(LR_instructions):
            i = 0
    is_end=True
    print(new_nodes)
    for node in new_nodes:
        if node[0][-1] != 'Z':
            is_end=False
            break
    if is_end:
        print(step)
        all_Z=True
    else:
        nodes=new_nodes