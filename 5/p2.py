from collections import defaultdict
from copy import copy

INPUT_FILE = 'input.txt'

def main():
    mid_sum = 0
    rules = defaultdict(set)
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            if line == '\n':
                break
            s_line = line.strip().split('|')
            bef, aft = int(s_line[0]), int(s_line[1])
            rules[bef].add(aft)

        bads = []
        for line in f:
            s_line = [int(e) for e in line.strip().split(',')]
            for i in range(len(s_line)):
                ele = s_line[i]
                if len(set(s_line[:i]).intersection(rules[ele])) > 0:
                    bads.append(s_line)
                    break
    for bad in bads:
        t_bad = copy(bad)
        good = []
        while len(t_bad) > 0:
            for t in range(len(t_bad)):
                if len(rules[t_bad[t]].intersection(set(t_bad[:t]+t_bad[t+1:]))) == 0:
                    good = [t_bad[t]] + good
                    t_bad.remove(t_bad[t])
                    break
        mid_sum += good[len(good)//2]
    print(mid_sum)

if __name__ == '__main__':
    main()