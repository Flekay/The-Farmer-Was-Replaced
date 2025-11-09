import os

# Folders to ignore during bundling
IGNORED_FOLDERS = {
    'sorting',
    'datatypes',
    'tests',
}

def generate_libraries_readme(libraries_dir, bundled_modules):
    """
    Generates a README.md file for the Libraries directory listing all bundled modules.
    """
    readme_path = os.path.join(libraries_dir, "README.md")

    # Module descriptions
    descriptions = {
        'builtins': 'Provides built-in utility functions',
        'dictionary': 'Functions for working with dictionaries',
        'farming': 'Functions related to farming operations',
        'list': 'Functions for working with lists',
        'logic_gates': 'Functions for implementing logic gates',
        'math': 'Functions for mathematical operations',
        'operations': 'Functions for performing operations',
        'random': 'Functions for generating random values',
        'scipy': 'Scientific computing functions',
        'string': 'Functions for working with strings',
        'sympy': 'Functions for symbolic mathematics and prime numbers',
        'typing': 'Functions related to type annotations'
    }

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Libraries\n\n")
        f.write("This folder contains the bundled Python modules generated from the \"General\" folder.\n\n")

        for module in sorted(bundled_modules):
            # Convert module name to title case for display
            display_name = module.replace("_", " ").title()
            # Get description or use default
            description = descriptions.get(module, f"Functions for {module.replace('_', ' ')} operations")
            # Create link to the original folder's README
            f.write(f"- [{display_name}](../General/{module}/): {description}.\n")

        f.write("\nRefer to each module for detailed information.\n")

def bundle_subfolders():
    """
    Bundles all Python files from subfolders in /General directory into single files in /Libraries.
    Ignores specified folders and markdown files.
    """
    general_dir = os.path.dirname(__file__)  # Current directory is General
    libraries_dir = os.path.join(os.path.dirname(__file__), "..", "Libraries")

    # Create libraries directory if it doesn't exist
    if not os.path.exists(libraries_dir):
        os.makedirs(libraries_dir)

    bundled_modules = []

    for folder in os.listdir(general_dir):
        if folder in IGNORED_FOLDERS or folder.startswith('.'):
            continue

        folder_path = os.path.join(general_dir, folder)
        if os.path.isdir(folder_path):
            bundled_modules.append(folder)
            output_file = os.path.join(libraries_dir, f"{folder}.py")
            with open(output_file, "w", encoding="utf-8") as out:
                files_in_folder = os.listdir(folder_path)
                py_files = [
                    f for f in files_in_folder
                    if os.path.isfile(os.path.join(folder_path, f))
                    and not f.endswith(".md")
                    and not f.startswith("__")
                    and not f.startswith(".")  # Ignore hidden files
                    and not f.startswith("test")
                ]
                if 'constants.py' in py_files:
                    py_files.remove('constants.py')
                    py_files.insert(0, 'constants.py')

                for file_name in py_files:
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, "r", encoding="utf-8") as f:
                        out.write(f.read())
                        out.write("\n")

    # Generate the README file
    generate_libraries_readme(libraries_dir, bundled_modules)

if __name__ == "__main__":
    bundle_subfolders()
