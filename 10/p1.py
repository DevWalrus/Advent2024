import re
from collections import deque

INPUT_FILE = 'input.txt'

def bfs(data: list[list[int]], start: tuple[int, int]):
    visited: set[tuple[int, int]] = set()
    queue: deque[tuple[int, int]] = deque([start])
    found = set()

    visited.add(start)
    while queue:
        current = queue.popleft()

        if data[current[0]][current[1]] == 9:
            found.add(current)

        for neighbor in [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1), (current[0], current[1] + 1)]:
            if 0 <= neighbor[0] < len(data) and 0 <= neighbor[1] < len(data[0]):
                if neighbor not in visited and data[neighbor[0]][neighbor[1]] == data[current[0]][current[1]] + 1:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return len(found)

def main():
    data = []
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            data.append([int(n) for n in list(line.strip())])

    starts = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                starts.append((i, j))

    print(sum([bfs(data, s) for s in starts]))



if __name__ == '__main__':
    main()