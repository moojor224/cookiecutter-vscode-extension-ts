import subprocess

subprocess.call(["git", "init"])
subprocess.call(
    [
        "git",
        "remote",
        "add",
        "origin",
        "https://github.com/{{cookiecutter.author}}/{{cookiecutter.extension_id}}.git",
    ]
)
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])
# subprocess.call(["npm", "install"])