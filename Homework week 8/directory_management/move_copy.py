import os
import shutil

os.makedirs("source_folder", exist_ok=True)
os.makedirs("target_folder", exist_ok=True)

with open("source_folder/test.txt", "w", encoding="utf-8") as file:
    file.write("File for moving and copying\n")

shutil.copy("source_folder/test.txt", "target_folder/test_copy.txt")
print("File copied")

shutil.move("source_folder/test.txt", "target_folder/test_moved.txt")
print("File moved")