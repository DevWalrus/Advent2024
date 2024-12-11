from tqdm import tqdm

INPUT_FILE = 'input.txt'

blink_stone_hist = {}
blink_hist = {}

def blink_stone(stone: int) -> tuple[int, ...]:
    if stone in blink_stone_hist:
        return blink_stone_hist[stone]

    if stone == 0:
        res = (1,)
    elif len((s_stone := str(stone))) % 2 == 0:
        res = (int(s_stone[:len(s_stone) // 2]), int(s_stone[len(s_stone) // 2:]))
    else:
        res = (stone * 2024,)

    blink_stone_hist[stone] = res
    return res

def blink(stone: int, cnt: int) -> list[int]:
    if cnt == 0:
        return [stone]
    if cnt % 5 == 0:
        print(cnt)
    if (stone, cnt) in blink_hist:
        return blink_hist[(stone, cnt)]

    single_blink = blink_stone(stone)
    res = []
    for s in single_blink:
        res += blink(s, cnt-1)

    blink_hist[(stone, cnt)] = res
    return res

def main():
    final_cnt = 0
    with open(INPUT_FILE, 'r') as f:
        stones = [int(s) for s in f.read().split()]
        for s in tqdm(stones):
            final_cnt += len(blink(s, 75))
    print(final_cnt)

if __name__ == '__main__':
    main()