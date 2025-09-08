import os
import shutil

users = os.listdir(r"C:\Users")

def downloads_organizer():
    for user in users:
        downloads_path = os.path.join(r"C:\Users", user, "Downloads")
        if os.path.exists(downloads_path):
            files = os.listdir(downloads_path)
            print(f"Contents of {downloads_path}: {files}")

            for file in files:
                file_type = os.path.splitext(file)[1][1:]
                folder_path = os.path.join(downloads_path, file_type)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                shutil.move(os.path.join(downloads_path, file), os.path.join(folder_path, file))


def remove_duplicates():
    def scan_and_remove_duplicates(directory):
        items = os.listdir(directory)
        seen = set()

        # Check if there are subdirectories
        has_subdirs = False
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                has_subdirs = True
                scan_and_remove_duplicates(item_path)  # Recursive function to go all the way in LOVE MR TRUYENS

        #Remove files after check 
        if not has_subdirs:
            for item in items:
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):  #Dont touch folders
                    if item in seen:
                        os.remove(item_path)  # Remove duplicate file
                        print(f"Removed duplicate: {item_path}")
                    else:
                        seen.add(item)

def remove_empty_folders():
    def remove_folders(directory):
        items = os.listdir(directory)
        if items == []:
            os.remove(directory)
        for item in items:
            item_path = os.path.join(directory,item)
            
                

