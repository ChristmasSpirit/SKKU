import sys

input = sys.stdin.readline
e, b = map(int, input().split())
c = list(map(int, input().split()))


def leftorright(a):
    if len(a) == 1:
        return a
    middle = (len(a) + 1) // 2
    left = leftorright(a[:middle])
    right = leftorright(a[middle:])
    lefter = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lefter.append(left[i])
            righter.append(left[i])
            i += 1
        else:
            lefter.append(right[j])
            righter.append(right[j])
            j += 1
    while i < len(left):
        lefter.append(left[i])
        righter.append(left[i])
        i += 1
    while j < len(right):
        lefter.append(right[j])
        righter.append(right[j])
        j += 1
    return lefter


righter = []
leftorright(c)
if len(righter) >= b:
    print(righter[b - 1])
else:
    print('-1')
