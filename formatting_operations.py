import re

class HeaderObject:
    def __init__(self, level, line_number, parent=None):
        self.level = level
        self.line_number = line_number
        self.parent = parent

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

def create_header_objects(lines):
    header_objects = []
    header_pattern = re.compile(r'^(#+)\s(.*)$')

    for line_number, line in enumerate(lines, start=1):
        match = header_pattern.match(line)
        if match:
            current_level = len(match.group(1))
            parent = None
            for header in reversed(header_objects):
                if header.level < current_level:
                    parent = header
                    break
            header_object = HeaderObject(current_level, line_number, parent)
            header_objects.append(header_object)

    return header_objects

def auto_decrease_levels(lines):
    header_objects = create_header_objects(lines)
    adjusted_lines = lines.copy()

    for header in header_objects:
        if header.parent is None:
            adjusted_lines[header.line_number - 1] = '# ' + adjusted_lines[header.line_number - 1].lstrip('#')
        else:
            new_level = header.parent.level + 1
            adjusted_lines[header.line_number - 1] = '#' * new_level + ' ' + adjusted_lines[header.line_number - 1].lstrip('#')

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