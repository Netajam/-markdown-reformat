# Markdown Header Reformatting Script

This script allows you to reformat the header levels in a Markdown file. It provides the following operations:

1. **Increase Header Levels**
   - Description: Increases the header levels in the Markdown file by a specified number of levels.
   - Usage: `python main.py --file_path <file_path> increase <levels>`
   - Arguments:
     - `--file_path`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
     - `<levels>`: Number of levels to increase the headers by (e.g., 1, 2, 3).
   - Example: `python main.py --file_path README.md increase 1`

2. **Decrease Header Levels**
   - Description: Decreases the header levels in the Markdown file by a specified number of levels.
   - Usage: `python main.py --file_path <file_path> decrease <levels>`
   - Arguments:
     - `--file_path`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
     - `<levels>`: Number of levels to decrease the headers by (e.g., 1, 2, 3).
   - Example: `python main.py --file_path README.md decrease 1`

3. **Auto Decrease Header Levels**
   - Description: Automatically decreases the header levels in the Markdown file to the lowest possible level based on the nesting structure.
   - Usage: `python main.py --file_path <file_path> auto_decrease`
   - Arguments:
     - `--file_path`: Path to the Markdown file. If not provided, the default file path from `config.py` will be used.
   - Example: `python main.py --file_path README.md auto_decrease`

## Configuration

The script uses a `config.py` file to store the default file path. If the `--file_path` argument is not provided when running the script, it will use the default file path specified in `config.py`.

To set the default file path, open the `config.py` file and modify the `default_file_path` variable:

```python
default_file_path = 'path/to/your/default/markdown/file.md'