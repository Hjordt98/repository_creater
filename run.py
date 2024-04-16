# %% [markdown]
# # Repository Creater
# 
# This program will allow the user to enter a name of a new repository they wish to create.
# The program wil lthen take the entered name, replace the white space with underscore _.
# The proram will then create a folder, a README.md file, and run git init withing the new folder.

# %% [markdown]
# # Print statements for default .gitignore file for different languages

# %% [markdown]
# # Step 1 - user input 
# 
# Whitespace will automaticlly replaced with _

# %%
user_input_repo_name = input("Enter name of new repository, whitespace will be replaced with underscore -->")
user_input_repo_name = user_input_repo_name.replace(" ", "_")
print(f'Repository to be created will be called:\n{user_input_repo_name}')

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
from strings_gitignore import gitignore_java, gitignore_python

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


