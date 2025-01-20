File Organizer Script

A Python script that organizes files in a specified directory into subfolders based on their file types. It also adds versioning to the file names based on the creation timestamp to avoid overwriting files with the same name.

Features

- Organizes files into subfolders such as Images, Documents, Audio, Videos, and Archives.
- Supports common file types like:
  - Images: .jpg, .png, .jpeg
  - Documents: .pdf, .docx, .txt, .ppt, .pptx
  - Audio: .mp3, .wav
  - Videos: .mp4, .mkv
  - Archives: .zip, .rar
- Adds versioning to filenames based on the creation date and time (e.g., filename_20250120_152030.pdf).
- Provides a simple GUI to let the user select the folder for organizing files.

Requirements

- Python 3.x
- Tkinter (for the file dialog)

Most Python installations come with tkinter pre-installed. If you don’t have it, you can install it using:

pip install tk

Usage

1. Clone the repository to your local machine:

   git clone https://github.com/your-username/file-organizer.git

2. Navigate to the project directory:

   cd file-organizer

3. Run the script:

   python organize_files.py

4. A file dialog will appear, asking you to select the folder you want to organize.
5. The script will process the files and organize them into subfolders based on their type.

Example:

If you select a folder containing the following files:
- image1.jpg
- document1.pdf
- song1.mp3

The script will organize them as:
- Images/image1_20250120_152030.jpg
- Documents/document1_20250120_152030.pdf
- Audio/song1_20250120_152030.mp3

Folder Structure:

/your-folder
    /Images
    /Documents
    /Audio
    /Videos
    /Archives

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

- This script utilizes Python's built-in os, shutil, and tkinter libraries for file handling and GUI support.
