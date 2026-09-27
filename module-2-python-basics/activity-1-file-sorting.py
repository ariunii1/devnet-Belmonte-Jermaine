"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Belmonte, Jermaine Christyles A.]
Date: [9/27/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[I made a script that sorts files based on their extentions]


============================================
KEY VOCABULARY
============================================
- os module: this can make your program communicate with your pc
- shutil module: this is the tool that actually moves or copies the files around.
- file path: exact location of files in your files. 
- directory: in other words, folder
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "Downloads_Folder"
images_folder = "Images_Folder"

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

for filename in os.listdir(source_folder):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        
        old_path = os.path.join(source_folder, filename)
        new_path = os.path.join(images_folder, filename)
        
        shutil.move(old_path, new_path)
        print(filename + " was moved to Images!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I tried moving a fiel to a folder that didnt exist. so the code didnt work]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
