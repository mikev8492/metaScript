
#!/usr/bin/env python3

import sys

def main():

    # Standard output example:
    test_output = "TEST Output: 123456789"
    sys.stdout.write("This is output data: {test_output}.\n")

    # Standard Error example:
    if not int(test_output):
    sys.stderr.write("ERROR: The output is not an integer.\n")

    # Redirecting output streams:
    # $ python3 script.py > stdout.txt 2> stderr.txt

if __name__=="__main__":
    main()

