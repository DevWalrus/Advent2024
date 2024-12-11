from tqdm import tqdm

INPUT_FILE = 'input.txt'

def blink(lst: list[int]) -> list[int]:
    new_stones = []
    for i in range(len(lst)):
        stone = lst[i]
        if stone == 0:
            new_stones.append(1)
        elif len((s_stone := str(stone))) % 2 == 0:
            new_stones.append(int(s_stone[:len(s_stone)//2]))
            new_stones.append(int(s_stone[len(s_stone)//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def main():
    with open(INPUT_FILE, 'r') as f:
        stones = [int(s) for s in f.read().split()]
        for _ in tqdm(range(25)):
            stones = blink(stones)
        print(len(stones))

if __name__ == '__main__':
    main()