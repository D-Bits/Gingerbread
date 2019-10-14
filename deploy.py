from subprocess import run

deploy = run(['pyinstaller', 'main.py', '-F', '-n', 'Gingerbread'])

if deploy.returncode == 0:
    input('Delpoyment succesful. Press enter to exit.')
else:
    input('WARNING: Deployment failed. Press enter to exit.')