import os
import shutil
import time
from datetime import datetime

# Define the source and destination directories
source_dir = r"C:\Users\USER\PycharmProjects\pythonProject"  # Replace with your source directory
backup_dir = r"E:\Projects (Web, Apps and Videography)\Python Backup"  # Replace with your backup directory

#Devffrey14

# Function to create a timestamped backup
def create_backup(source, destination):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a new backup folder with the timestamp
    backup_folder = os.path.join(destination, f"backup_{timestamp}")

    try:
        # Copy the entire source directory to the new backup folder
        shutil.copytree(source, backup_folder)
        print(f"Backup completed successfully! Backup stored at: {backup_folder}")
    except Exception as e:
        print(f"Error during backup: {e}")


# Main execution
if __name__ == "__main__":
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
    else:
        # Ensure the backup directory exists, if not create it
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Perform the backup
        create_backup(source_dir, backup_dir)
