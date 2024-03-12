# Rename files

This python script renames every file in every folder within the directory to `folder_xxx`, where `xxx` increments from 0.

## Usage

Simply put this script in the main folder location and run it, i.e.

```
main_folder
|- main.py
|- folder_1
  |- file_xyz
  |- file_987
|- folder_2
  |- file_abc
```

will be renamed to

```
main_folder
|- main.py
|- folder_1
  |- folder_1_000
  |- folder_1_001
|- folder_2
  |- folder_2_002
```

## To do

- Now the files are renamed arbitrarily, we can implement a version to sort the files in a certain way first, then rename them.
- The script skips a number when incrementing if a non-file is detected.
- Let user to select the path when running the script, instead of having to place it in the root folder.
