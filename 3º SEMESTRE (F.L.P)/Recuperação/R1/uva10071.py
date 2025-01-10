import sys

for line in sys.stdin:
    v, t = map(int, line.split())
    deslocamento = 2 * v * t
    print(deslocamento)