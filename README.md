# TextFilterFuzzer
TextFilterFuzzer For Directory Fuzzing - filter for (e.g, Not Found, 404, Not Accepted) Simple but very effective to use. 

# Usage
python3 textfuzzer.py

Enter URL: https://evil.com

Enter the path to the wordlist file: /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt

Enter the filter text separated by comma (e.g., 'Not Found,406 Not Accepted'): Not Found, 404, Not Accepted

Now only URLs will printed to the terminal that don't match the "Not Found", "404, "Not Accepted" with the status code.

# Why?
Because from my experience when I'm using ffuf or any other tool for fuzzing, I can only exclude by code and size but sometimes the webpage may have the same code, size and content length but displays something different on the webpage itself, so this tool is designed to filter out the text directly from the webpage so you may find something that wasn't discovered using ffuf or feroxbuster. ;)

# PoC Demo - My tool vs ffuf in action

https://github.com/HackShiv/TextFilterFuzzer/assets/107373873/27075dcc-d188-4aae-8ed5-4a0801a1abd4

# Next steps
- To add FUZZ option

- To make it faster with larger wordlists   

If you find this simple tool useful or interesting. Do consider a star and follow on my github ;)

# Donations ❤️
<a href="https://www.buymeacoffee.com/hackshiv" target="_blank"><img src="https://uc18a5d6fa18c7a6e6bcf0c8ac68.previews.dropboxusercontent.com/p/thumb/ACSeWjaYon3DD9ybIl1P0_kUMesC-433mJdEs6lWeL4Ff_4trWI-XsOTC6s3Z6iVNaKRXjVXGhIj3WcJuVMVk1BJDj1EHgJWuk0KfKIV1QcQ8iRJlFbD0WuJAj26Bquqhh65f5_7LlaLRmoBETr8GrXy1CqKeATM49xaGG1WZJKfiwKMUfaBklfajnIwqVMOIxYT7cwKqz39KHsj3OpVpY-vdnRyAhr6R350TFwvTGYJm36Wm3nmH6RjUya1ozVpN07d8Vs4TY0nQguKwqQYhgE_rAXvrQsCSPMAaKGYrNECDE88vnLnRiErq8O1lKsoHZLoo37fg4EBK1vG8SWBr0So/p.png" alt="Buy Me A Coffee" height="41" width="174"></a>

