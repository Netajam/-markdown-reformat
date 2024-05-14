import argparse
from formatting_operations import reformat_markdown_file ,check_header_levels
from config import default_file_path
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reformat Markdown headers')
    parser.add_argument('-f', '--file', type=str, help='Path to the Markdown file')
    parser.add_argument('op', type=str, choices=['i', 'd', 'ad'], help='Operation to perform on headers (i: increase, d: decrease, ad: auto decrease)')
    parser.add_argument('n', type=int, nargs='?', default=1, help='Number of levels to increase or decrease')
    parser.add_argument('-s', '--start', type=int, help='Start line number for formatting')
    parser.add_argument('-e', '--end', type=int, help='End line number for formatting')

    args = parser.parse_args()

    file_path = args.file or default_file_path

    # Convert backslashes to forward slashes
    file_path = file_path.replace('\\', '/')

    print(f"File to be reformatted: {file_path}")

    warning_message = None
    if args.op in ['i', 'd']:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        warning_message = check_header_levels(lines, 'increase' if args.op == 'i' else 'decrease', args.n)

    if warning_message:
        print(warning_message)
    confirmation = input("Do you want to proceed? (Y/N): ")
    if confirmation.upper() != 'Y':
        print("Reformatting canceled.")
        exit()

    operation = 'increase' if args.op == 'i' else 'decrease' if args.op == 'd' else 'auto_decrease'
    reformat_markdown_file(file_path, operation, args.n, args.start, args.end)
    print("Reformatting completed.")