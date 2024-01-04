data = [line.split(',') for line in open('day15.txt', 'r').readlines()][0]
# print(data)


suma=0
for d in data:
    current_value = 0
    for x in d:
        current_value=((current_value+ord(x))*17)%256
    # print(current_value)
    suma+=current_value
print(suma)
