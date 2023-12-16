data = open("test.txt", 'r').read().split('\n\n')
data = open("day5.txt", 'r').read().split('\n\n')
seeds = [int(x) for x in data[0].split(':')[1].strip().split()]
seeds_soil = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[1].split(':')[1].strip().split('\n'))]
soil_fertilizer = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[2].split(':')[1].strip().split('\n'))]
fertilizer_water = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[3].split(':')[1].strip().split('\n'))]
water_light = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[4].split(':')[1].strip().split('\n'))]
light_temperature = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[5].split(':')[1].strip().split('\n'))]
temperature_humidity = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[6].split(':')[1].strip().split('\n'))]
humidity_location = [[int(x), int(y), int(z)] for x,y,z in (d.split() for d in data[7].split(':')[1].strip().split('\n'))]

# print(data)
# destination, source, range
print(seeds)
print(seeds_soil)
print(soil_fertilizer)
print(fertilizer_water)
print(water_light)
print(light_temperature)
print(temperature_humidity)
print(humidity_location)

combined_data=[seeds_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]
combined_data_reverse = list(reversed(combined_data))
def get_destination_from_source(source, map):
    for line in map:
        if line[1] <= source <= (line[1]+line[2]):
            return line[0]+(source-line[1])
    return source

def get_source_from_destination_part(destination, map):
    for line in map:
        if line[0] <= destination <= (line[0]+line[2]):
            return line[1]+(destination-line[0])
    return destination

def get_source_from_destination(destination):
    output = destination
    for i in range(len(combined_data_reverse)):
            output=get_source_from_destination_part(output, combined_data_reverse[i])
    return output

print()
# print(get_destination_from_source(52, seeds_soil))
# print()
def part1():
    locations=[]
    for seed in seeds:
        output=seed
        # print(output, end=' ')
        for i in range(len(combined_data)):
            output=get_destination_from_source(output, combined_data[i])
            # print(output, end=' ')
        locations.append(output)
    print(min(locations))

def part2():
    all_seeds = []
    for i in range(0,len(seeds)-1, 2):
        for s in range(seeds[i], seeds[i]+seeds[i+1]):
            all_seeds.append(s)
    for i in range(10000000000):
        seed=get_source_from_destination(i)
        if seed in all_seeds:
            return i

print(part2())
print()
# print(get_source_from_destination_part(46, humidity_location))
# print(get_source_from_destination_part(46, temperature_humidity))
# print(get_source_from_destination_part(45, light_temperature))
# print(get_source_from_destination_part(77, water_light))
# print(get_source_from_destination_part(84, fertilizer_water))
# print(get_source_from_destination_part(84, soil_fertilizer))
# print(get_source_from_destination_part(84, seeds_soil))