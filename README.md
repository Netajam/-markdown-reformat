# Markdown Header Reformatting Script

This script allows you to reformat the header levels in a Markdown file. It provides the following operations:

1. **Increase Header Levels**
   - Description: Increases the header levels in the Markdown file by a specified number of levels.
   - Usage: `python main.py -f <file> i [n]`
   - Arguments:
     - `-f` or `--file`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
     - `i`: Indicates the increase operation.
     - `n`: (Optional) Number of levels to increase the headers by (e.g., 1, 2, 3). Default is 1.
   - Example: `python main.py -f README.md i 2`

2. **Decrease Header Levels**
   - Description: Decreases the header levels in the Markdown file by a specified number of levels.
   - Usage: `python main.py -f <file> d [n]`
   - Arguments:
     - `-f` or `--file`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
     - `d`: Indicates the decrease operation.
     - `n`: (Optional) Number of levels to decrease the headers by (e.g., 1, 2, 3). Default is 1.
   - Example: `python main.py -f README.md d 1`

3. **Auto Decrease Header Levels**
   - Description: Automatically decreases the header levels in the Markdown file to the lowest possible level based on the nesting structure.
   - Usage: `python main.py -f <file> ad`
   - Arguments:
     - `-f` or `--file`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
     - `ad`: Indicates the auto decrease operation.
   - Example: `python main.py -f README.md ad`

## Additional Options

- **Start Line** (`-s` or `--start`): Specifies the start line number for formatting. Only lines starting from this line number will be reformatted.
- **End Line** (`-e` or `--end`): Specifies the end line number for formatting. Only lines up to this line number will be reformatted.

Example: `python main.py -f README.md -s 10 -e 20 ad`

This command will apply the 'auto_decrease' operation to the lines between line numbers 10 and 20 (inclusive) in the specified file.

## Configuration

The script uses a `config.py` file to store the default file path. If the `-f` or `--file` argument is not provided when running the script, it will use the default file path specified in `config.py`.

To set the default file path, open the `config.py` file and modify the `default_file_path` variable:

```python
default_file_path = 'path/to/your/default/markdown/file.md'