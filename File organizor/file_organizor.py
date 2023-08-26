import shutil as shu
import os

print('''This program will collect all files (image files, MP3 files, MP4 files, PDF files, text files, Excel files, and zip files) and move them to separate directories.\n''')

dirp = input("Enter the path of the Directory: ")

# Collect all the files from the directory
files = os.listdir(dirp)
dir = dirp + "/"

# Types of files that are possible in that directory
types = {
    ".mp3": "musics",
    ".mp4": "videos",
    ".img": "images",
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".webp": "images",
    ".pdf": "pdf_files",
    ".txt": "text_files",
    ".ppt": "ppt_files",
    ".pptx": "ppt_files",
    ".docx": "doc_files",
    ".xlsx": "excel_files",
    ".zip": "zip_files",
    ".rar": "zip_files",
    ".7z": "zip_files"
}

# Function to return key for any value
def get_key(val):
    for key, value in types.items():
        if val == value:
            return key
    return "Key doesn't exist"

# Iterate through all the files to check and move them to the respective directories
for f in files:
    file_ext = os.path.splitext(f)[1]
    if file_ext in types:
        target_dir = dir + types[file_ext]
        print(f)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        shu.move(dir + f, os.path.join(target_dir, f))
        print("\n\tFile moved successfully!!\n")
