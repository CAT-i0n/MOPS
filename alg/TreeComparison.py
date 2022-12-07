import zss

def zss_comparison(algTree, tree1, tree2):
    diff = zss.simple_distance(
        tree1, tree2, algTree.get_children, algTree.get_label)
    dlen = abs(tree1.size - tree2.size)
    absd = diff - dlen
    return (diff, dlen, (tree1.size - absd)/tree1.size,
            (tree2.size - absd)/tree2.size)

#change None with algorithm function
def another_comparison(SyntaxTree, tree1, tree2):
    return zss.simple_distance(
        tree1, tree2, SyntaxTree.get_children, SyntaxTree.get_label, None)
