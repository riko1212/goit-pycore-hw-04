import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_tree(path, indent=""):
    try:
        directory = Path(path)

        if not directory.exists():
            print(f"Error: The path '{path}' does not exist.")
            return

        if not directory.is_dir():
            print(f"Error: The path '{path}' is not a directory.")
            return

        items = sorted(directory.iterdir(), key=lambda x: x.is_file())
        
        for item in items:
            if item.is_dir():
                print(indent + Fore.BLUE + Style.BRIGHT + "📂 " + item.name)
                print_directory_tree(item, indent + "    ")
            else:
                print(indent + Fore.GREEN + "📜 " + item.name)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_directory>")
    else:
        path_to_directory = sys.argv[1]
        print_directory_tree(path_to_directory)
