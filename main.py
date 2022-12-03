from loader.projectLoad import prepare_projects
from tree.Python3Builder import algTree
from alg.TreeComparison import zcc_comparison

if __name__ == "__main__":
    tree1 = algTree()
    project1_path = r'tree/test.py'
    tree1.root(project1_path)

    tree2 = algTree()
    project2_path = r'tree/test2.py'
    tree2.root(project2_path)
    
    print(zcc_comparison(algTree, tree1, tree2))
    
