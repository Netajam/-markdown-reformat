import re

def adjust_header_level(line, operation, levels):
    header_pattern = re.compile(r'^(#+)\s(.*)$')
    match = header_pattern.match(line)
    if match:
        current_level = len(match.group(1))
        title = match.group(2)
        if operation == 'increase':
            new_level = min(current_level + levels, 6)
        elif operation == 'decrease':
            new_level = max(current_level - levels, 1)
        else:
            raise ValueError(f"Invalid operation: {operation}")
        return '#' * new_level + ' ' + title + '\n'
    return line

def check_header_levels(lines, operation, levels):
    max_level = 0
    min_level = float('inf')
    for line in lines:
        header_pattern = re.compile(r'^(#+)\s(.*)$')
        match = header_pattern.match(line)
        if match:
            current_level = len(match.group(1))
            max_level = max(max_level, current_level)
            min_level = min(min_level, current_level)

    if operation == 'increase':
        if max_level + levels > 6:
            return f"Warning: Increasing the header levels by {levels} will result in headers exceeding the maximum level of 6."
    elif operation == 'decrease':
        if min_level - levels < 1:
            return f"Warning: Decreasing the header levels by {levels} will result in losing some headers."
    return None

def find_parent_level(lines, index):
    for i in range(index - 1, -1, -1):
        header_pattern = re.compile(r'^(#+)\s(.*)$')
        match = header_pattern.match(lines[i])
        if match:
            return len(match.group(1))
    return 0

def auto_decrease_levels(lines):
    header_pattern = re.compile(r'^(#+)\s(.*)$')
    adjusted_lines = lines.copy()

    for i in range(len(lines) - 1, -1, -1):
        match = header_pattern.match(lines[i])
        if match:
            current_level = len(match.group(1))
            parent_level = find_parent_level(lines, i)
            if current_level - parent_level > 1:
                adjusted_level = parent_level + 1
                adjusted_lines[i] = '#' * adjusted_level + ' ' + match.group(2) + '\n'

    return adjusted_lines

def reformat_markdown_file(file_path, operation, levels):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    warning_message = check_header_levels(lines, operation, levels)
    if warning_message:
        return warning_message

    if operation == 'auto_decrease':
        reformatted_lines = auto_decrease_levels(lines)
    else:
        reformatted_lines = [adjust_header_level(line, operation, levels) for line in lines]

    with open(file_path, 'w') as file:
        file.writelines(reformatted_lines)

    return None