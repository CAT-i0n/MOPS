import os
import click
from loader.projectLoad import prepare_projects
from tree.Python3Builder import algTree
from alg.TreeComparison import zcc_comparison


@click.group()
def start() -> None:
    pass

@start.command("show")
def show() -> None:
    print("Test")


@start.command("load_and_compare")
@click.option('-f', '--first', default="None", help="first project git url")
@click.option('-s', '--second', default="None", help="second project git url")
def compareProjects(first: str, second: str):
    prepare_projects(first, second)
    tree1 = algTree()
    project1_path = r'firstComparedProject.py'
    tree1.root(project1_path)

    tree2 = algTree()
    project2_path = r'secondComparedProject.py'
    tree2.root(project2_path)

    print(zcc_comparison(algTree, tree1, tree2))


@start.command("load")
@click.option('-f', '--first', default="None", help="first project git url")
@click.option('-s', '--second', default="None", help="second project git url")
def compareProjects(first: str, second: str):
    prepare_projects(first, second)


@start.command("compare")
def compareProjects():
    tree1 = algTree()
    project1_path = r'firstComparedProject.py'
    tree1.root(project1_path)

    tree2 = algTree()
    project2_path = r'secondComparedProject.py'
    tree2.root(project2_path)

    print(zcc_comparison(algTree, tree1, tree2))


if __name__ == "__main__":
    start()
