# "Meta-Script" Generator

## Overview:
 Bioinformaticians often write dozens of small scripts. Starting from a blank file every time is inefficient and leads to missing best practices (like forgetting the shebang or the main block).

 This tool contains a Python3 script `scaffold.py` that generates a formatted Python3 template file in the `output` folder. 

 ## Instructions:
  Run the following script and enter desired filename.
 ```
 ./scaffold.py
 ``` 

 ## Script details:
 1. `template_content` contains the template code for the new file stored as a string. 
 2. The user is prompted to enter a filename. 
 3. The filename is sanitized for invalid characters and added to the `output/` folder path. 
 4. If the filename already exists in the folder, the user is prompted to overwrite or abort. 
 5. The `template_content` is written to the new file. 

