data = open("test.txt", 'r').readlines()
data = open("day4.txt", 'r').readlines()
data = [[x, y] for x, y in (d.split(':') for d in data)]
data_tmp=[]
for d, n in data:
    x, y = d.split()
    l=[[x, int(y)]]
    n=n.strip().split('|')
    winning_number=[int(x) for x in n[0].split()]
    my_number=[int(x) for x in n[1].split()]
    l.append(winning_number)
    l.append(my_number)
    # print(l)
    data_tmp.append(l)
data=data_tmp
# print(data)
def calculate_points(winning_number, my_number):
    points = 0
    for number in my_number:
        if number in winning_number:
            if points==0:
                points=1
            else:
                points*=2
    return points

def number_of_matches(winning_number, my_number):
    matches = 0
    for number in my_number:
        if number in winning_number:
            matches+=1
    return matches

def get_cart_by_number(number):
    for d in data:
        if d[0][1]==number:
            return d

def get_card_number(card):
    return card[0][1]
def part1():
    suma=0
    for d in data:
        suma+=calculate_points(d[1], d[2])
    return suma

def part2():
    for d in data:
        nb_matches = number_of_matches(d[1], d[2])
        card_number = get_card_number(d)
        for x in range(card_number+1, card_number+nb_matches+1):
            data.append(get_cart_by_number(x))
    return(len(data))
# print(part1())
print(part2())