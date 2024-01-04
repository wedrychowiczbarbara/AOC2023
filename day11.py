data = [x.strip() for x in open("day11.txt", "r").readlines()]

def read_data():
    new_data=[]
    for d in data:
        line=[]
        for i in range(len(d)):
            if d[i]=='.':
                line.append(0)
            else:
                line.append(1)
        new_data.append(line)
    return new_data
def check_column(column_nb, data):
    all_empty_spaces = True
    for i in range(len(data)):
        if data[i][column_nb]==1:
            all_empty_spaces=False
            break
    return all_empty_spaces

def check_row(row_nb, data):
    all_empty_spaces = True
    for i in range(len(data[0])):
        if data[row_nb][i]==1:
            all_empty_spaces=False
            break
    return all_empty_spaces

data=read_data()
for d in data:
    print(d)

row=[]
column=[]

for i in range(len(data)):
    if check_row(i, data):
        # t=[0]*len(data[0])
        # data.insert(i, t)
        row.append(i+len(row))
        print(i)

print()
for i in range(len(data[0])):
    if check_column(i, data):
        # for j in range(len(data)):
        #     data[j].insert(i, 0)
        print(i)
        column.append(i+len(column))

for i in row:
    t=[0]*len(data[0])
    data.insert(i, t)
for i in column:
    for j in range(len(data)):
        data[j].insert(i, 0)
for d in data:
    print(d)

galaxy_coordinates = []

for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col]==1:
            galaxy_coordinates.append([row,col])
        #row, col
print(galaxy_coordinates)

sum_dist=0
for g1 in galaxy_coordinates:
    for g2 in galaxy_coordinates:
        sum_dist+=(abs(g1[0]-g2[0])+abs(g1[1]-g2[1]))
print(int(sum_dist/2))
#6,1 -> 11,5 (11-6 + 5-1)9