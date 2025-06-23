import subprocess

try:
    subprocess.check_call(["git", "init"])
    # subprocess.call(
    #     [
    #         "git",
    #         "remote",
    #         "add",
    #         "origin",
    #         "https://github.com/{{cookiecutter.author}}/{{cookiecutter.extension_id}}.git",
    #     ]
    # )
    subprocess.check_call(["git", "add", "."])
    subprocess.check_call(["git", "commit", "-m", "Initial commit"])
except subprocess.CalledProcessError:
    pass # ignore error if git not installed

try:
    subprocess.check_call(["npm", "install"])
except (subprocess.CalledProcessError, FileNotFoundError):
    pass # ignore error if npm not installed
