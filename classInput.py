#! /usr/bin/python3
## reads in file and writes out normalized data

def class_array():
    f = open('class.csv', 'r')
    read_array = []
    for line in f:
        line = line.strip()
        read_array.append(line.split(','))
    f.close()
        
#day        weekday = 0, saturday = .33, sunday =.66, holiday = 1;
#seasons    summer = 0, autumn = .33, winter =.66, spring = 1;
#wind       none = 0, normal = .5, high = 1;
#Rain       none = 0, slight = .5, heavy = 1;
#answer     cancelled = 0, very late = .33, late = .66, on time = 1;
    normalized_array = []
    entry=[]
    for list in read_array:
        for s in list:
            if s == 'weekday' or s == 'summer' or s == 'none' or s == 'cancelled':
                entry.append(0)
            elif s == 'saturday' or s == 'autumn' or s == 'very late':
                entry.append(.33)
            elif s == 'normal' or s == 'slight':
                entry.append(.5)
            elif s == 'sunday' or s == 'winter' or s == 'late':
                entry.append(.66)
            elif s == 'holiday' or s == 'spring' or s == 'on time' or s == 'heavy' or s == 'high':
                entry.append(1)
        if entry:
            normalized_array.append(entry)
        entry = []

    return normalized_array
