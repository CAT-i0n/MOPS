import sys
sys.path.append('../')
#from com.load_project import prepare_projects
from tree.TreeBuilder import SyntaxTree
from alg.TreeComparison import zss_comparison

if __name__ == "__main__":
    tree1 = SyntaxTree()
    project1_path = r'examples/test.py'
    tree1.root(project1_path, simplify = True)
    
    tree2 = SyntaxTree()
    project2_path = r'examples/test2.py'
    tree2.root(project2_path, simplify = True)
    print(tree1.size)
    print(tree2.size)
    rez = zss_comparison(SyntaxTree, tree1, tree2)
    print(rez)
    print(f'similarity is {max(rez[2], rez[3])*100} percents')
    
    
