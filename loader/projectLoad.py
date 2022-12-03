from git import Repo
import os
import re


def prepare_projects(first_git_url, second_git_url):
    first_compared_project = "firstComparedProject"
    second_compared_project = "secondComparedProject"
    Repo.clone_from(first_git_url, first_compared_project)
    Repo.clone_from(second_git_url, second_compared_project)
    concatenation(first_compared_project, "firstComparedProject.py")
    concatenation(second_compared_project, "secondComparedProject.py")


def concatenation(path, concatenation_file_name):
    project_files = []
    for path, subdirs, files in os.walk(path):
        for name in files:
            project_files.append(os.path.join(path, name))
    python_project_files = []
    for project_file in project_files:
        if project_file[-3:] == ".py":
            python_project_files.append(project_file)

    with open(concatenation_file_name, 'w') as concatenation_file:
        for file_name in python_project_files:
            with open(file_name, 'r') as read_file:
                for line in read_file:
                    line_split = re.split(' |,|\n', line)
                    if "import" == line_split[0]:
                        new_str = 'import '
                        for index in range(len(line_split) - 1):
                            if line_split[index + 1] == '':
                                continue
                            import_file_name = line_split[index + 1].replace(".", "\\") + ".py"
                            if not import_file_name in python_project_files:
                                new_str += line_split[index + 1] + ', '
                        new_str = new_str[:-2] + '\n'
                        concatenation_file.write(new_str)
                    elif "from" == line_split[0]:
                        import_file_name = line_split[1].replace(".", "\\") + ".py"
                        if not import_file_name in python_project_files:
                            concatenation_file.write(line)
                    else:
                        concatenation_file.write(line)
                concatenation_file.write('\n')
