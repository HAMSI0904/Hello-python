# Hello-python
print("Hello, world")
import requests

url = "https://raw.githubusercontent.com/HAMSI0904/Hello-python/main/Hello.py"
response = requests.get(url)

if response.status_code == 200:
    script_content = response.text
    print("Script fetched successfully:\n")
    print(script_content)
else:
    print("Failed to fetch the script. Status code:", response.status_code)
