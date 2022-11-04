from com.load_project import prepare_projects
from tree.Python3Builder import algTree
from tree.Python3Lexer import Python3Lexer
from tree.Python3Parser import Python3Parser


if __name__ == "__main__":
    tree1 = algTree()
    project1_path = r'D:\CourcePr\MOPS\tree\test.py'
    tree1.root(project1_path)

    tree2 = algTree()
    project2_path = r'D:\CourcePr\MOPS\tree\test2.py'
    tree2.root(project2_path)
