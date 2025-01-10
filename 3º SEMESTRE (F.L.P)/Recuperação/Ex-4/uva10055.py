from sys import stdin

for line in stdin:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    print(abs(a - b))