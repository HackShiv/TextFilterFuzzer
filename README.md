# Textfuzzer
TextFilterFuzzer For Directory Fuzzing - filter for (e.g, Not Found, 404, Not Accepted) Simple but very effective to use. 

# Usage
python3 textfuzzer.py

Enter URL: https://evil.com

Enter the path to the wordlist file: /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt

Enter the filter text separated by comma (e.g., 'Not Found,406 Not Allowed'): Not Found, 404, Not Accepted

Now only URLs will printed to the terminal that don't match the "Not Found", "404, "Not Accepted" with the status code.

# Why?
Because from my experience when I'm using ffuf or any other tool for fuzzing, I can only exclude by code and size but sometimes the webpage may have the same code, size and content length but displays something different on the webpage itself, so this tool is designed to filter out the text directly from the webpage so you may find something that wasn't discovered using ffuf. ;)

Also star this if you find it useful. Thanks.

