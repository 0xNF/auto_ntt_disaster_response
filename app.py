#!/usr/bin/env python
import src.parse_from_thunderbird as tb
import src.launch_selenium as ls
import sys, os

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./eml")

def get_most_recent_file(directory: str):
    # Get list of files in the directory
    files = os.listdir(directory)

    # Get file paths along with their creation times
    file_creation_times = [(os.path.join(directory, file), os.path.getctime(os.path.join(directory, file))) for file in files]

    # Sort files by creation time in descending order
    file_creation_times.sort(key=lambda x: x[1], reverse=True)

    if len(file_creation_times) == 0:
        return None
    else:
        # Get the most recently created file
        most_recent_file_path, most_recent_creation_time = file_creation_times[0]
        return most_recent_file_path
    
def clear_dir(directory: str):
    files = os.listdir(directory)
    for file in files:
        p = os.path.join(directory, file)
        os.unlink(p)

def read_file(p) -> str:
    with open(p, 'r') as f:
        return f.read()

def main() -> int:
    mrf = get_most_recent_file(directory)
    if mrf is None:
        return 1
    text = read_file(mrf)
    urlmatch = tb.parseMessageBody(text)
    if urlmatch is None:
        return 1
    print(f'Found url: {urlmatch}')
    ls.launch_browser(urlmatch)
    clear_dir(directory)
    return 0
    

if __name__ == "__main__":
    sys.exit(main())