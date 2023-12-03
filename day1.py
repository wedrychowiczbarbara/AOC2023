data = [x.strip() for x in open("day1.txt", 'r').readlines()]
# data = [x.strip() for x in open("test.txt", 'r').readlines()]
print(data)
def get_first_number(line):
    for i in range(len(line)):
        try:
            nb=int(line[i])
            return [nb, i]
        except:
            continue
    return [0, 0]

def get_last_number(line):
    for i in range(len(line)):
        try:
            nb=int(line[len(line)-(i+1)])
            return [nb, len(line)-(i+1)]
        except:
            continue
    return [0,0]

def part1():
    suma=0
    for line in data:
        number=(get_first_number(line)[0]+10*get_last_number(line)[0])
        suma+=number
    print(suma)

def find_min(list):
    min=list[0][1]
    min_val=list[0][0]
    for x,y in list:
        if y<min:
            min=y
            min_val=x
    return min_val

def find_max(list):
    max=list[0][1]
    max_val=list[0][0]
    for x,y in list:
        if y>max:
            max=y
            max_val=x
    return max_val

def part2():
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    suma=0
    for line in data:
        nr_list=[]
        for nr in numbers:
            if nr in line:
                for i in range(len(line)-len(nr)+1):
                    if line[i:i+len(nr)]==nr:
                        nr_list.append([numbers_dict[nr], i])
        nr_list.append(get_first_number(line))
        nr_list.append(get_last_number(line))
        # print(nr_list, end=' ')
        suma+=(10*find_min(nr_list)+find_max(nr_list))

    print(suma)
