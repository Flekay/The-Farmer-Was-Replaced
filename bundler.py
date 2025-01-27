import os

# Folders to ignore during bundling
IGNORED_FOLDERS = {
    'sorting',
    'pathing',
}

def bundle_subfolders():
    """
    Bundles all Python files from subfolders in /general directory into single files in /libraries.
    Ignores specified folders and markdown files.
    """
    general_dir = os.path.join(os.path.dirname(__file__), "general")
    libraries_dir = os.path.join(os.path.dirname(__file__), "libraries")

    # Create libraries directory if it doesn't exist
    if not os.path.exists(libraries_dir):
        os.makedirs(libraries_dir)

    # Create general directory if it doesn't exist
    if not os.path.exists(general_dir):
        os.makedirs(general_dir)

    for folder in os.listdir(general_dir):
        if folder in IGNORED_FOLDERS:
            continue

        folder_path = os.path.join(general_dir, folder)
        if os.path.isdir(folder_path):
            output_file = os.path.join(libraries_dir, f"{folder}.py")
            with open(output_file, "w", encoding="utf-8") as out:
                files_in_folder = os.listdir(folder_path)
                py_files = [
                    f for f in files_in_folder
                    if os.path.isfile(os.path.join(folder_path, f))
                    and not f.endswith(".md")
                ]
                if 'constants.py' in py_files:
                    py_files.remove('constants.py')
                    py_files.insert(0, 'constants.py')

                for file_name in py_files:
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, "r", encoding="utf-8") as f:
                        out.write(f.read())
                        out.write("\n")

if __name__ == "__main__":
    bundle_subfolders()
