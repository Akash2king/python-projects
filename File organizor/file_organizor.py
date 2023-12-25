import shutil as shu
import os
import platform

print('''This program will collect all files (image files, MP3 files, MP4 files, PDF files, text files, Excel files, and zip files) and move them to separate directories.\n''')

dirp = input("Enter the path of the Directory: ")

# Collect all the files from the directory
files = os.listdir(dirp)
dir = dirp + os.path.sep

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
    ".7z": "zip_files",
    ".py": "python_files",
    ".c": "c_files",
    ".java": "java_files",
    ".html": "html_files",
    ".css": "css_files",
    ".js": "javascript_files",
    ".json": "json_files",
    ".xml": "xml_files",
    ".csv": "csv_files",
    ".log": "log_files",
    ".sql": "sql_files",
    ".md": "markdown_files",
    ".sh": "shell_files",
    ".exe": "executable_files",
    ".dll": "dll_files",
    ".apk": "android_files",
    ".ipa": "ios_files",
    ".deb": "debian_files",
    ".rpm": "redhat_files",
    ".woff": "font_files",
    ".ttf": "font_files",
    ".otf": "font_files",
    ".wav": "audio_files",
    ".ogg": "audio_files",
    ".flac": "audio_files",
    ".aac": "audio_files",
    ".m4a": "audio_files",
    ".avi": "video_files",
    ".mkv": "video_files",
    ".flv": "video_files",
    ".mov": "video_files",
    ".wmv": "video_files",
    ".svg": "vector_images",
    ".eps": "vector_images",
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
        shu.move(os.path.join(dir, f), os.path.join(target_dir, f))
        print("\n\tFile moved successfully!!\n")

print("\nOperation completed successfully!")
