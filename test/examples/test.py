def GraphKernelComparison(tree1,tree2,measure=0):
    if tree1.get_children()==[] or tree2.get_children()==[]:
        return measure
    queue1=deque()
    queue2=deque()
    s1=set()
    a=1
    add(queue1,[tree1])
    while len(queue1)>0:
        a=a+1
        el1 =queue1.popleft()
        add(queue1,el1.get_children())
        add(queue2,[tree2])
        while len(queue2)>0:
            el2 = queue2.popleft()
            if el1.get_label()==el2.get_label() and  (el1.get_label() not in s1):
                measure=measure+1
                s1.add(el2.get_label())
            add(queue2,el2.get_children())
    return measure

def comparison(first, second) -> ComparisonResult:
    globalMatchs = []
    for startFirst in range(len(first)):
        for startSecond in range(len(second)):
            length = 0
            while first[startFirst + length] == second[startSecond + length]:
                length += 1
                if startSecond + length >= len(second):
                    break
                if startFirst + length >= len(first):
                    break
            if length > 1:
                m = Match()
                m.startFirst = startFirst
                m.startSecond = startSecond
                m.length = length
                addMatchIfNotOverlapping(globalMatchs, m)
    return ComparisonResult(first, second, globalMatchs)
