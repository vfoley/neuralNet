#! /usr/bin/python3
## reads in file and writes out normalized data
def weather_array():
    f = open('weather.csv', 'r')
    read_array = []
    for line in f:
        line = line.strip()
        read_array.append(line.split(','))
    f.close()

        
#outlook rain = 0, overcast = .5, sun = 1;
#temperature cool = 0, mild = .5, hot = 1;
#humidity normal = 0, high = 1;
#windy  False = 0, true = 1;
#answer no = 0, yes = 1;
    normalized_array = []
    entry=[]
    for list in read_array:
        for s in list:
            if s == 'rainy' or s == 'cool' or s == 'normal' or s == 'FALSE' or s == 'no':
                entry.append(0)
            elif s == 'overcast' or s == 'mild':
                entry.append(.5)
            elif s == 'sunny' or s == 'hot' or s == 'high' or s == 'TRUE' or s == 'yes':
                entry.append(1)
        if entry:
            normalized_array.append(entry)
        entry = []

    return normalized_array
