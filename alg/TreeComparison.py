import zss
def zcc_comparison(algTree, tree1, tree2):
    return zss.simple_distance(
        tree1, tree2, algTree.get_children, algTree.get_label)