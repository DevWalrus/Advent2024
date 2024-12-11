import re

INPUT_FILE = 'input.txt'

def rec_calc(lst: list[int]):
    if len(lst) == 1:
        return [str(lst[0])]
    elem = lst[0]
    all_strs = []
    for inner in rec_calc(lst[1:]):
        all_strs.append(f'{elem}+{inner}')
        all_strs.append(f'{elem}*{inner}')
    return all_strs

def custom_eval(equ: str, goal: int) -> int:
    first_num = re.search(r'\d+', equ).group()
    equ = equ[len(first_num):]
    total = int(first_num)
    while len(equ) > 0:
        op = equ[0]
        equ = equ[1:]
        num = re.search(r'\d+', equ).group()
        if op == '+':
            total += int(num)
        if op == '*':
            total *= int(num)
        equ = equ[len(num):]
    return total == goal


def main():
    total = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            s_line = line.strip().split(':')
            goal, nums = int(s_line[0]), [int(n) for n in s_line[1].split()]
            # print(goal, nums)
            if any([custom_eval(s, goal) for s in rec_calc(nums)]):
                total += goal
    print(total)


if __name__ == '__main__':
    main()