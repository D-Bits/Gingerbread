from subprocess import run
from os import chdir
from cutters import(
    data_eng_cc, 
    php_cc, 
    django_cc, 
    asp_cc, 
    flask_cc, 
    static_cc, 
    django_rest_and_vue
) 
from git import git_auto

""" Store the users options for project 
generation in a dictionary """
u_options = {
    0: 'Cookiecutter from a GitHub repo of your choosing',
    1: 'Python3 Data Engineering Project',
    2: 'Django & PostgreSQL Project',
    3: 'ASP.NET Core MVC Site.',
    4: 'PHP Website.',
    5: 'Flask Web Application.',
    6: 'Simple, static site.',
    7: 'A Django REST and Vue.js RESTful project.',
}


if __name__ == "__main__":
    
    try:
        print()
        print("Welcome to Gingerbread! A CLI-based front-end for Cookiecutter.\n")

        proj_dir = input("Enter the full path to directory where you want your project to be stored (Ex: /home/documents/projects): ")

        # Don't let the user enter a null value for the dir
        if proj_dir is None:
            input('Must specify a director')

        chdir(proj_dir)

        # Blank line for readability
        print()

        for key, val in u_options.items():

            print(key, val)

        print()

        u_choice = int(input('Enter an integer, based on the above options: '))

        if u_choice is None:
            print("Error: Must choose an option!")

        if u_choice == 0:
            repo_url = input("Enter the URL, or local path, of your template's repository: ")
            run(['cookiecutter', repo_url], check=True)
        elif u_choice == 1:
            run(['cookiecutter', data_eng_cc], check=True)
        elif u_choice == 2:
            run(['cookiecutter', django_cc], check=True)
        elif u_choice == 3: 
            run(['cookiecutter', asp_cc], check=True)
        elif u_choice == 4:
            run(['cookiecutter', php_cc], check=True)
        elif u_choice == 5:
            run(['cookiecutter', flask_cc], check=True)
        elif u_choice == 6:
            run(['cookiecutter', static_cc], check=True)
        elif u_choice == 7:
            run(['cookiecutter', django_rest_and_vue], check=True)
        else:
            input('Invalid input. Press enter to exit.')
        
        input('Project generation completed. Press enter to exit.')

    except FileNotFoundError:

        input("Error: Cannot find directory.")
