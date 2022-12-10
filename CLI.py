import click

from alg.GraphKernelComparison import percent
from alg.StringComparison import comparison
from alg.TokenTypeComparison import printComparisonReport
from loader.projectLoad import prepare_projects
from alg.TreeComparison import zss_comparison
from tree.TreeBuilder import SyntaxTree


project1_path = r'firstComparedProject.py'
project2_path = r'secondComparedProject.py'


@click.group()
def start() -> None:
    pass


@start.command("load")
@click.option('-f', '--first', default="None", help="first project git url")
@click.option('-s', '--second', default="None", help="second project git url")
def loadProjects(first, second):
    prepare_projects(first, second)


@start.command("graph_compare")
def graphCompareProjects():
    try:
        tree1 = SyntaxTree()
        tree1.root(project1_path)

        tree2 = SyntaxTree()
        tree2.root(project2_path)
        print("Plagiarism rate: ", percent(tree1, tree2))
    except FileNotFoundError:
        print("Projects don't load")


@start.command("string_compare")
def stringCompareProjects():
    try:
        with open(project1_path) as file:
            project1_text = file.read()

        with open(project2_path) as file:
            project2_text = file.read()

        print("Plagiarism rate: ", comparison(project1_text, project2_text))
    except FileNotFoundError:
        print("Projects don't load")


@start.command("tree_compare")
def treeCompareProjects():
    try:
        tree1 = SyntaxTree()
        tree1.root(project1_path, simplify=True)

        tree2 = SyntaxTree()
        tree2.root(project2_path, simplify=True)
        rez = zss_comparison(SyntaxTree, tree1, tree2)
        print("Plagiarism rate: ", {max(rez[2], rez[3])*100})
    except FileNotFoundError:
        print("Projects don't load")


@start.command("token_compare")
def tokenCompareProjects():
    try:
        printComparisonReport(project1_path, project2_path)
    except FileNotFoundError:
        print("Projects don't load")


if __name__ == "__main__":
    start()
