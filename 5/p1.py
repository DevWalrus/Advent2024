from collections import defaultdict

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
        for line in f:
            s_line = [int(e) for e in line.strip().split(',')]
            bad = False
            for i in range(len(s_line)):
                ele = s_line[i]
                if len(set(s_line[:i]).intersection(rules[ele])) > 0:
                    bad = True
                    break
            if not bad:
                mid_sum += s_line[len(s_line)//2]
    print(mid_sum)


if __name__ == '__main__':
    main()