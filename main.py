
def findSubsets(array):
    subsets = []
    for i in range(2**len(array)):
        subsets.append([])

    for idx, item in enumerate(array):
        gap = 2**idx
        x = 0
        for i in range(2**len(array)):
            if x == (gap * 2):
                x = 1
            else:
                if x < gap:
                    x += 1
                else:
                    subsets[i].append(item)
                    x += 1
    
    return subsets

findSubsets([1, 2, 3])
