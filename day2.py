data = open("day2.txt", 'r').readlines()
# data = open("test.txt", 'r').readlines()
data = [x.strip().split(':') for x in data]
data = [[x, y.strip().split(';')] for x, y in data]
print(data)
data_tmp = []
for d in data:
    game_name=d[0].split()
    splited_rounds=[]
    for rounds in d[1]:
        sr=rounds.split(',')
        sr2=[]
        for s in sr:
            r=s.strip().split()
            sr2.append([int(r[0]), r[1]])
        splited_rounds.append(sr2)
    data_tmp.append([[game_name[0], int(game_name[1])], splited_rounds])
data=data_tmp
print(data)

def is_enough_cubes(cubes):
    if cubes[1]=='red' and cubes[0]>12:
        return False
    elif cubes[1]=='green' and cubes[0]>13:
        return False
    elif cubes[1]=='blue' and cubes[0]>14:
        return False
    else:
        return True

def part1():
    sum_game_name=0
    for game in data:
        is_enough = True
        for rounds in game[1]:
            for r in rounds:
                if not is_enough_cubes(r):
                    is_enough=False
                    break
        if is_enough:
            sum_game_name+=game[0][1]
    print(sum_game_name)

def part():
    suma=0
    for game in data:
        red=0
        green=0
        blue=0
        for rounds in game[1]:
            for r in rounds:
                if r[1]=='red' and r[0]>red:
                    red=r[0]
                elif r[1]=='green' and r[0]>green:
                    green=r[0]
                elif r[1]=='blue' and r[0]>blue:
                    blue=r[0]
        suma+=(red*green*blue)
    print(suma)
