def comparison(first, second) -> ComparisonResult:
    globalMatchs = []
    for startFirst in range(len(first)):
        for startSecond in range(len(second)):
            length = 0

def GraphKernelComparison(tree1,tree2,measure=0):
    if tree1.get_children()==[] or tree2.get_children()==[]:
        return measure
    queue1=deque()
    queue2=deque()
    s1=set()