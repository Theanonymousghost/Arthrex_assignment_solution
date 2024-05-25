from collections import deque

candidates = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z'],
}

contacted = []
current = deque()


def contacted_candidates(char):
    if char in candidates:
        current.append(char)
        current.extend(candidates[char])
    else:
        for key, value in candidates.items():
            if char in value:
                current.extend(candidates[key])
                current.append(key)

    while current:
        temp = current.popleft()
        if temp in contacted:
            continue
        else:
            contacted.append(temp)
            if temp in candidates:
                current.extend(candidates[temp])


ins = input("Input char: ")
contacted_candidates(ins)
print(contacted)
