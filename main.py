import argparse
from formatting_operations import reformat_markdown_file
from config import default_file_path
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reformat Markdown headers')
    parser.add_argument('--file_path', type=str, help='Path to the Markdown file')
    parser.add_argument('operation', type=str, choices=['increase', 'decrease', 'auto_decrease'], help='Operation to perform on headers')
    parser.add_argument('levels', type=int, nargs='?', default=1, help='Number of levels to increase or decrease')

    args = parser.parse_args()

    file_path = args.file_path or default_file_path

    # Convert backslashes to forward slashes
    file_path = file_path.replace('\\', '/')

    print(f"File to be reformatted: {file_path}")

    warning_message = None
    if args.operation in ['increase', 'decrease']:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        warning_message = check_header_levels(lines, args.operation, args.levels)

    if warning_message:
        print(warning_message)
    confirmation = input("Do you want to proceed? (Y/N): ")
    if confirmation.upper() != 'Y':
        print("Reformatting canceled.")
        exit()

    reformat_markdown_file(file_path, args.operation, args.levels)
    print("Reformatting completed.")