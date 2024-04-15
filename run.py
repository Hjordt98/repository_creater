#!/usr/bin/env python
# coding: utf-8

# # Repository Creater
# 
# This program will allow the user to enter a name of a new repository they wish to create.
# The program wil lthen take the entered name, replace the white space with underscore _.
# The proram will then create a folder, a README.md file, and run git init withing the new folder.

# # Step 1 - user input 
# 
# Whitespace will automaticlly replaced with _

# In[26]:


user_input = input("Enter name of new repository, whitespace will be replaced with underscore")

user_input = user_input.replace(" ", "_")

print(f'Repository to be created will be called: {user_input}')


# # Step 2 - creation of repository in folder and README.md file

# In[27]:


import os

folder_target = "C:\\Users\\andre\\Documents\\VSCode\\"

folder_user_input_target = folder_target + user_input

os.mkdir(folder_user_input_target)

readme_file_location = os.path.join(folder_user_input_target, "README.md")

with open(readme_file_location, 'w') as readme_file:
    readme_file.write("# README")
    readme_file.close


# # Step 3 - initalize it as a git project

# In[28]:


import subprocess

subprocess.run(["git", "init"], cwd=folder_user_input_target)

