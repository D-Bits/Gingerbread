from subprocess import run
from os import chdir
from cutters import data_eng_cc, php_cc, django_cc, asp_cc, flask_cc, static_cc
from git import git_auto

""" Store the users options for project 
generation in a dictionary """
u_options = {
    1: 'Cookiecutter from a GitHub repo of your choosing',
    2: 'Python3 Data Engineering Project',
    3: 'Django & PostgreSQL Project',
    4: 'ASP.NET Core MVC Site.',
    5: 'PHP Website.',
    6: 'Flask Web Application.',
    7: 'Simple, static site.',
}


if __name__ == "__main__":
    
    print()
    print("Welcome to Gingerbread! A CLI-based front-end for Cookiecutter.\n")

    proj_dir = input("Enter the full path to directory where you want your project to be stored (Ex: /home/documents/projects): ")
    chdir(proj_dir)

    # Blank line for readability
    print()

    for key, val in u_options.items():

        print(key, val)

    print()

    u_choice = int(input('Enter an integer, based on the above options: '))

    if u_choice == 1:
        repo_url = input("Enter the URL of your template's repository: ")
        run(['cookiecutter', repo_url], check=True)
        git_auto()
    elif u_choice == 2:
        run(['cookiecutter', data_eng_cc], check=True)
        git_auto()
    elif u_choice == 3:
        run(['cookiecutter', django_cc], check=True)
        git_auto()
    elif u_choice == 4: 
        run(['cookiecutter', asp_cc], check=True)
        git_auto()
    elif u_choice == 5:
        run(['cookiecutter', php_cc], check=True)
        git_auto()
    elif u_choice == 6:
        run(['cookiecutter', flask_cc], check=True)
        git_auto()
    elif u_choice == 7:
        run(['cookiecutter', static_cc], check=True)
        git_auto()
    else:
        input('Invalid input. Press enter to exit.')
    
    input('Project generation completed. Press enter to exit.')
