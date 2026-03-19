# Example 3: copy and delete file safely

import shutil
import os

with open("original.txt", "w", encoding="utf-8") as file:
    file.write("This is the original file\n")

shutil.copy("original.txt", "backup.txt")
print("File copied")

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("Backup deleted")
else:
    print("Backup file not found")