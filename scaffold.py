#!/usr/bin/env python3
import sys, re
from pathlib import Path

# Python3 Template file contents:
template_content = """
#!/usr/bin/env python3

import sys, argparse
import pandas as pd


def create_parser() -> argparse.ArgumentParser:
    # Create and configure the argument parser.

    # Returns:
    #     A configured ArgumentParser instance with all supported
    #     command-line arguments.
    
    parser = argparse.ArgumentParser(
        description="Parses expression data and generates statistics.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="gene_expression_mutations.csv",
        help="Export to file",
    )

    return parser


def validate_arguments(args: argparse.Namespace) -> None:
    # Validate parsed command-line arguments.

    # Checks that all parameter values are within their valid ranges
    # and that constraints between parameters are satisfied.

    # Args:
    #     args: Parsed argument namespace from argparse.

    # Raises:
    #     ValueError: If any argument is invalid or constraints are
    #         violated (e.g., min-length > max-length).
    
    out_path = Path(args.output)

    if out_path.is_file():
        usr_ans = input("\nThe output file already exists, overwrite? (y/n)\n")
        if usr_ans == "n":
            raise IOError("\nExecution cancelled\n")
    

def main():
    try:
        parser = create_parser()
        args = parser.parse_args()

        print("test")

    except ValueError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    except IOError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1



if __name__=="__main__":
    sys.exit(main())

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

