from collections import defaultdict
from tqdm import tqdm

INPUT_FILE = 'input.txt'

BLINK_HIST = {}

def blink(stone: int, cnt: int) -> list[int]:
    global BLINK_HIST
    if cnt == 0:
        return [stone]
    if (stone, cnt) in BLINK_HIST:
        return BLINK_HIST[(stone, cnt)]

    for i in range(cnt-1, 0, -1):
        if (stone, i) in BLINK_HIST:
            res = blink_all_stones(BLINK_HIST[(stone, i)], cnt-i)
            BLINK_HIST[(stone, cnt)] = res
            return res

    if stone == 0:
        single_blink = (1,)
    elif len((s_stone := str(stone))) % 2 == 0:
        single_blink = (int(s_stone[:len(s_stone) // 2]), int(s_stone[len(s_stone) // 2:]))
    else:
        single_blink = (stone * 2024,)

    res = []
    for s in single_blink:
        res += blink(s, cnt-1)

    BLINK_HIST[(stone, cnt)] = res
    return res

def blink_all_stones(stones, cnt):
    res = []
    for s in stones:
        res += blink(s, cnt)
    return res

def clean_mem():
    max_bs = defaultdict(int)
    for b, cnt in BLINK_HIST.keys():
        if max_bs[b] < cnt:
            max_bs[b] = cnt
    all_keys = list(BLINK_HIST.keys())
    for b, cnt in all_keys:
        if max_bs[b] != cnt and cnt >= 10:
            BLINK_HIST.pop((b, cnt))

def main():
    with open(INPUT_FILE, 'r') as f:
        stones = [int(s) for s in f.read().split()]
        for s in tqdm(stones):
            blink(s, 30)
        clean_mem()
        for s in tqdm(stones):
            blink(s, 45)
        clean_mem()
        for i in range(46, 75):
            for s in tqdm(stones, desc=str(i)):
                blink(s, i)
            clean_mem()
        final_cnt = 0
        for s in tqdm(stones):
            final_cnt += len(blink(s, 75))
        print(final_cnt)

if __name__ == '__main__':
    main()