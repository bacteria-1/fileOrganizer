import os
import shutil

# Define file categories and their destination paths
FILE_DESTINATIONS = {
    "Videos": ([".mp4", ".mkv", ".avi", ".mov", ".flv"], os.path.expanduser("~/Movies")),
    "Audio": ([".mp3", ".wav", ".aac", ".flac", ".ogg"], os.path.expanduser("~/Music")),
    "Images": ([".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"], os.path.expanduser("~/Pictures")),
    "Executables": ([".exe", ".msi", ".bat", ".sh", ".apk"], os.path.expanduser("~/Tools")),
    "Compressed": ([".zip", ".rar", ".tar", ".gz", ".7z"], os.path.expanduser("~/Compressed")),
    "Documents": ([".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".html"], os.path.expanduser("~/Documents")),
}

# Source folder (Downloads)
SOURCE_DIRECTORY = os.path.expanduser("~/Downloads")

def organize_files(source_directory):
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' not found.")
        return
    
    # Loop through each file in the source directory
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(file)

        # Delete unfinished downloads (.crdownload)
        if file_extension.lower() == ".crdownload":
            os.remove(file_path)
            print(f"Deleted unfinished download: {file}")
            continue

        # Find the correct destination for the file
        for category, (extensions, destination) in FILE_DESTINATIONS.items():
            if file_extension.lower() in extensions:
                if not os.path.exists(destination):  # Create destination folder if it doesn't exist
                    os.makedirs(destination)

                # Move file to the appropriate folder
                shutil.move(file_path, os.path.join(destination, file))
                print(f"Moved: {file} → {destination}/")
                break  # Stop checking once a match is found

if __name__ == "__main__":
    organize_files(SOURCE_DIRECTORY)
    print("File sorting complete!")
