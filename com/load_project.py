from git import Repo


def prepare_projects(first_git_url, second_git_url):
    first_compared_project = "firstComparedProject"
    second_compared_project = "secondComparedProject"
    Repo.clone_from(first_git_url, first_compared_project)
    Repo.clone_from(second_git_url, second_compared_project)

