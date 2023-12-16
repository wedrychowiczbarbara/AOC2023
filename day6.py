'''
whole_time
record_distance
charge_time
speed = charge_time
move_time = whole_time - charge_time
distance = move_time*speed
distance = (whole_time - charge_time)*charge_time
y=(b-x)*x    y=bx-x^2
y' = b-2x
b-2x = 0
x=b/2
range -> 0, whole_time

y = b/4

y=(b-x)*x > record_distance
'''
import math

data=[[62, 553], [64, 1010], [91, 1473],[90, 1074]]
data2=[62649190, 553101014731074]
def max_distance(whole_time):
    return(whole_time - round(whole_time / 2)) * round(whole_time / 2)
def charge_time_for_max_distance(whole_time):
    return math.ceil(whole_time / 2)

def distance_by_charge_time(whole_time, charge_time):
    distance = (whole_time - charge_time) * charge_time
    return distance

def winning_range_size(whole_time, record_distance):
    max_charge_time = charge_time_for_max_distance(whole_time)
    distance = distance_by_charge_time(whole_time, max_charge_time)
    counter=0
    while distance>record_distance:
        counter+=1
        max_charge_time-=1
        distance=distance_by_charge_time(whole_time, max_charge_time)
    max_charge_time = charge_time_for_max_distance(whole_time)
    distance = distance_by_charge_time(whole_time, max_charge_time)
    while distance>record_distance and max_charge_time<whole_time:
        counter+=1
        max_charge_time+=1
        distance=distance_by_charge_time(whole_time, max_charge_time)
    return counter-1

def part1():
    nb_ways_to_win=1
    for time, record_distance in data:
        nb_ways_to_win*=winning_range_size(time, record_distance)
    print(nb_ways_to_win)

def part2():
    nb_ways_to_win = 1
    nb_ways_to_win *= winning_range_size(data2[0], data2[1])
    print(nb_ways_to_win)

part2()