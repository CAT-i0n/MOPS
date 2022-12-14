def split(arr, k: int):
    rez = []
    for start in range(len(arr) - k + 1):
        r = ''
        for i in range(k):
            r = r + arr[start + i]
        rez.append(r)
    return r, rez
def compress(arr, k, w):
    arr = split(arr, k)
    arr = hashs(arr)
    arr = mins(arr, w)
    return arr[1]
@cache
def min_i(arr, start, length, p):
    min_v = arr[start]
    rez = start
    for i in range(start+1, start+length):
        value = arr[i]
        if value <= min_v:
            rez = i
            min_v = value
    return rez[1]
def comparison(first, second, k = 5, w = 4):
    second = compress(second, k, w)
    first = compress(first, k, w)
    return base_comparison(first, second).similarity()
def mins(arr, w:int):
    rez = []
    g_i = -1
    for start in range(len(arr) - w + 1):
        i = min_i(arr, start, w)
        if i != g_i:
            g_i = i
            rez.append(arr[i])
    return rez

    