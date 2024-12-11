import re
from collections import deque

INPUT_FILE = 's_input.txt'

def all_dots(s:str) -> bool:
    for i in s:
        if i != '.':
            return False
    return True

def main():
    with open(INPUT_FILE, 'r') as f:
        raw_data = [int(n) for n in list(f.read().strip())]

    is_space = False
    n_id = 0
    data = ''
    for n in raw_data:
        if is_space:
            data += '.'*n
        else:
            data += str(n_id)*n
            n_id += 1
        is_space = not is_space

    result = ''
    while not all_dots(data):
        # print(result, data)
        if data[0].isdigit():
            to_move = re.findall(r'\d+', data)[0]
            result += to_move
            data = data[len(to_move):]
        else:
            to_fill = re.findall(r'\.+', data)[0]
            data = data[len(to_fill):]
            for i in range(len(to_fill)):
                while True:
                    filler = data[-1]
                    data = data[:-1]
                    if filler.isdigit():
                        break
                result += filler
    print(result, data)
    print(sum([i*int(j) for i,j in enumerate(result)]))





if __name__ == '__main__':
    main()