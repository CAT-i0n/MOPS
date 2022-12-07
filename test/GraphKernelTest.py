import sys
sys.path.append('../')
#from com.load_project import prepare_projects
from tree.TreeBuilder import SyntaxTree
from alg.GraphKernelComparison import GraphKernelComparison,percent

if __name__ == "__main__":
    tree1 = SyntaxTree()
    project1_path = r'examples/test.py'
    tree1.root(project1_path)

    tree2 = SyntaxTree()
    project2_path = r'examples/test2.py'
    tree2.root(project2_path)
    print(GraphKernelComparison( tree1, tree2))
    print(percent(tree1,tree2))