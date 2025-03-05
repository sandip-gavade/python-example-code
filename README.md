# python-example-code

python practice code

set up pipenv environment

pipenv --version

mkdir pipenv_project && cd pipenv_project

pipenv --python 3.12 # Use your Python version

This will create:

A Pipfile (to manage dependencies)
A Pipfile.lock (to lock dependency versions)

Step 4: Set Virtual Environment in the Current Directory
By default, Pipenv stores virtual environments in ~/.local/share/virtualenvs/. To keep it inside your project folder, run:

export PIPENV_VENV_IN_PROJECT=1
pipenv install

Step 5: Activate the Virtual Environment
pipenv shell
