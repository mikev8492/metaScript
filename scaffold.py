#!/usr/bin/env python3
import sys, re
from pathlib import Path

# Python3 Template file contents:
template_content = """
#!/usr/bin/env python3

import sys

def main():

    # Standard output example:
    test_output = "TEST Output: 123456789"
    sys.stdout.write("This is output data: {test_output}.\\n")

    # Standard Error example:
    if not int(test_output):
    sys.stderr.write("ERROR: The output is not an integer.\\n")

    # Redirecting output streams:
    # $ python3 script.py > stdout.txt 2> stderr.txt

if __name__=="__main__":
    main()

"""

def main():
    # Ask for output filename:
    fileName = input("Enter a filename to generate a Python3 template:\n").strip()

    # Sanitize for invalid filename characters:
    invalid_chars = re.compile(r'[\\/:*?"<>|]')
    while (invalid_chars.search(fileName)):
        fileName = input("Invalid characters used, Re-enter a filename to generate a Python3 template:\n").strip()

    # Add python extension to filename:
    if ".py" not in fileName:
        fileName = fileName + ".py"

    # Use Path object to set output:
    output_path = Path("output") / fileName

    # Check if file already exists:
    if output_path.exists():
        usr_response = input(f"'{output_path}' already exists. Overwrite file? [y/n]\n").strip().lower()

        if usr_response != "y":
            sys.stderr.write(f"Aborted. '{output_path}' was not overwritten.\n")
            sys.exit(1)
    
    # Create directory (if doesnt exist) and write file:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template_content)

    sys.stdout.write(f"\nNew File '{output_path}' created!\n")

if __name__=="__main__":
    main()

