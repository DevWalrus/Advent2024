import re

INPUT_FILE = 'input.txt'
REGEX_STR = r'mul\(([0-9]+),([0-9]+)\)'

total = 0
with open(INPUT_FILE, 'r') as f:
    line = f.read()
    print(line)
    for match in re.finditer(REGEX_STR, line):
        total += int(match.group(1))*int(match.group(2))
print(total)