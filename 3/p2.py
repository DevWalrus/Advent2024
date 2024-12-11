import re

INPUT_FILE = 'input.txt'
REGEX_STR = r'mul\(([0-9]+),([0-9]+)\)'
GOOD_CMD = 'do()'
BAD_CMD = 'don\'t()'

def calc_line(line: str) -> int:
    total = 0
    for match in re.finditer(REGEX_STR, line):
        total += int(match.group(1)) * int(match.group(2))
    return total

def main():
    total = 0
    with open(INPUT_FILE, 'r') as f:
        bad_lines = f.read().split(BAD_CMD)
        total += calc_line(bad_lines[0])
        for neg_line in bad_lines[1:]:
            if (good_idx := neg_line.find(GOOD_CMD)) == -1:
                continue
            good_line = neg_line[good_idx + len(GOOD_CMD):]
            print(good_line)
            total += calc_line(good_line)
    print(total)

if __name__ == '__main__':
    main()