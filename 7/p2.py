import re

INPUT_FILE = 's_input.txt'
OPS = {
    '+': lambda x, y: int(x) + int(y),
    '*': lambda x, y: int(x) * int(y),
    '||': lambda x, y: int(str(x) + str(y)),
}

def rec_calc(lst: list[int]):
    if len(lst) == 1:
        return [str(lst[0])]
    elem = lst[0]
    all_strs = []
    for inner in rec_calc(lst[1:]):
        for op in OPS:
            all_strs.append(f'{elem}{op}{inner}')
    return all_strs

def custom_eval(equ: str, goal: int) -> int:
    first_num = re.search(r'\d+', equ).group()
    equ = equ[len(first_num):]
    total = int(first_num)

    while len(equ) > 0:
        op = re.search(r'\D+', equ).group()
        equ = equ[len(op):]

        num = re.search(r'\d+', equ).group()
        equ = equ[len(num):]

        total = OPS[op](total, num)

    return total == goal

def main():
    total = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            s_line = line.strip().split(':')
            goal, nums = int(s_line[0]), [int(n) for n in s_line[1].split()]
            if any([custom_eval(s, goal) for s in rec_calc(nums)]):
                total += goal
    print(total)


if __name__ == '__main__':
    main()