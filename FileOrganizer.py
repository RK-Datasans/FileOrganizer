import os
import shutil
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def get_directory():
    # Open a GUI window to let the user select a folder
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory(title="Select Folder to Organize")
    return folder_selected

def add_version_to_filename(filepath):
    # Add a version to the filename based on the file's creation time
    timestamp = os.path.getctime(filepath)
    creation_time = datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M%S')
    dirname, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}_{creation_time}{ext}"
    return os.path.join(dirname, new_filename)

def organize_files(directory):
    file_types = {
        "Images": ['.jpg', '.png', '.jpeg'],
        "Documents": ['.pdf', '.docx', '.txt', '.ppt', '.pptx'],
        "Audio": ['.mp3', '.wav'],
        "Videos": ['.mp4', '.mkv'],
        "Archives": ['.zip', '.rar']
    }

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            for folder, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    # Check for versioning before moving the file
                    new_filepath = add_version_to_filename(filepath)
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(filepath, new_filepath)
                    shutil.move(new_filepath, folder_path)
                    break

# Ask the user to select the directory
directory = get_directory()
if directory:
    organize_files(directory)
else:
    print("No directory selected.")
