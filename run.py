# %% [markdown]
# # Repository Creater
# 
# This program will allow the user to enter a name of a new repository they wish to create.
# The program wil lthen take the entered name, replace the white space with underscore _.
# The proram will then create a folder, a README.md file, and run git init withing the new folder.

# %% [markdown]
# # Print statements for default .gitignore file for different languages

# %%
gitignore_java = """
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
replay_pid*
"""


gitignore_python = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
# """


# %% [markdown]
# # Step 1 - user input 
# 
# Whitespace will automaticlly replaced with _

# %%
user_input_repo_name = input("Enter name of new repository, whitespace will be replaced with underscore --> ")
user_input_repo_name = user_input_repo_name.replace(" ", "_")
print(f'Repository to be created will be called:{user_input_repo_name}')


user_input_gitignore = input(
"""Do you want a default .gitignore fill to be created for one of the below mentioned languages? 
Please enter the corresponding number and press enter. Or type 0 if you dont want a .gitignore file
1 - Java
2 - Python
0 - I dont want a .gitignore file to be created
""")

# %% [markdown]
# # Step 2 - creation of folder and files

# %%
import os

folder_target = "C:\\Users\\andre\\Documents\\VSCode\\"

folder_user_input_target = folder_target + user_input_repo_name

os.mkdir(folder_user_input_target)

readme_file_location = os.path.join(folder_user_input_target, "README.md")

with open(readme_file_location, 'w') as readme_file:
    readme_file.write("# README")
    readme_file.close
    
if user_input_gitignore == '1':
    gitignore_file_location = os.path.join(folder_user_input_target, ".gitignore")
    with open(gitignore_file_location, 'w') as gitignore_file:
        gitignore_file.write(gitignore_java)
        gitignore_file.close
elif user_input_gitignore == '2':
    gitignore_file_location = os.path.join(folder_user_input_target, ".gitignore")
    with open(gitignore_file_location, 'w') as gitignore_file:
        gitignore_file.write(gitignore_python)
        gitignore_file.close
elif user_input_gitignore == '0':
    pass
else:
    print("Error in input, no .gitignore file will be created")
        

# %% [markdown]
# # Step 3 - initalize it as a git project

# %%
import subprocess

subprocess.run(["git", "init"], cwd=folder_user_input_target)


