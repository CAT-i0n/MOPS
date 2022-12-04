from git import Repo, rmtree
import os
import re


def prepare_projects(first_git_url, second_git_url):
    first_compared_project = "firstComparedProject"
    second_compared_project = "secondComparedProject"
    rmtree('secondComparedProject')
    try:
        rmtree('firstComparedProject')
    except FileNotFoundError:
        pass
    try:
        rmtree('secondComparedProject')
    except FileNotFoundError:
        pass

    Repo.clone_from(first_git_url, first_compared_project)
    Repo.clone_from(second_git_url, second_compared_project)
    concatenation(first_compared_project, "firstComparedProject.py")
    concatenation(second_compared_project, "secondComparedProject.py")


def concatenation(project_path, concatenation_file_name):
    project_files_paths = []
    project_files_names = []

    for path, subdirs, files in os.walk(project_path):
        for name in files:
            project_files_paths.append(os.path.join(path, name))
            project_files_names.append(name)

    python_project_files_paths = []
    python_project_files_names = []

    for project_file in project_files_paths:
        if project_file[-3:] == ".py":
            python_project_files_paths.append(project_file)

    for project_file in project_files_names:
        if project_file[-3:] == ".py":
            python_project_files_names.append(project_file)

    with open(concatenation_file_name, 'w') as concatenation_file:
        for file_name in python_project_files_paths:
            with open(file_name, 'r') as read_file:
                for line in read_file:
                    line_split = re.split(' |,|\n', line)
                    if "import" == line_split[0]:
                        new_str = 'import '
                        for index in range(len(line_split) - 1):
                            if line_split[index + 1] == '':
                                continue
                            import_file_name = line_split[index + 1].split(".")[-1] + ".py"
                            if not import_file_name in python_project_files_names:
                                new_str += line_split[index + 1] + ', '
                        new_str = new_str[:-2] + '\n'
                        concatenation_file.write(new_str)
                    elif "from" == line_split[0]:
                        import_file_name = line_split[1].split(".")[-1] + ".py"
                        if not import_file_name in python_project_files_names:
                            concatenation_file.write(line)
                    else:
                        concatenation_file.write(line)
                concatenation_file.write('\n')
