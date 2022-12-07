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