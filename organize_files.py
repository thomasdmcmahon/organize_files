import os
import shutil
import re
import argparse

def create_directory(path):
    """Create a new directory at the given path if it doesn't already exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def get_file_list(organize_directory):
    """Get a list of files in the directory"""
    with os.scandir(organize_directory) as entries:
        for entry in entries:
            if not entry.is_dir():
                yield entry

def validate_file_name(file_name):
    """Validate file name with regex"""
    filename_pattern = r"^(Screenshot \d{4}-\d{2}-\d{2} at \d{2}\.\d{2}\d.(A-Z-a-z))*" # Matches the pattern of macOS screenshots; regex needs updated for different file name patterns
    return re.match(filename_pattern, file_name)

def move_file(file_path, destination_path):
    """Move file from current location to destination. If a conflict is detected, the file is renamed rather than replaced"""
    try:
        if os.path.exists(destination_path):
            base, ext = os.path.splitext(destination_path)
            i = 0
            while os.path.exists(destination_path):
                i += 1
                destination_path = f"{base}_{i}{ext}"

        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} to {destination_path}")

    except Exception as e:
        print(f"Failed to move {file_path}. Error: {e}")


def organize_files(organize_directory, to_folder):
    """Go through all files in the specified directory, and move the ones that pass file name validation to target directory"""
    moveto_directory = os.path.join(organize_directory, to_folder)
    create_directory(moveto_directory)

    for entry in get_file_list(organize_directory):
        file_name = entry.name
        file_path = entry.path
        if validate_file_name(file_name):
            destination_path = os.path.join(moveto_directory, file_name)
            move_file(file_path, destination_path)

if __name__ == "__main__":
    """Parse command-line arguments and run the file organizer."""
    parser = argparse.ArgumentParser(description="Organize files.")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("target", help="Target directory")
    args = parser.parse_args()
    organize_files(args.source, args.target)
