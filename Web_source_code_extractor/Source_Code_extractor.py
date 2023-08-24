import requests
import re

def extract_source_code(url):
    response = requests.get(url)
    if response.status_code == 200:
        source_code = response.text
    else:
        source_code = f"Error fetching source code for {url}. Status code: {response.status_code}"
    return source_code

def save_source_code_as_file(source_code, filename):
    with open(filename, "w") as file:
        file.write(source_code)
        print(f"File '{filename}' written successfully!")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    source_code = extract_source_code(url)

    pattern = r"https://(.*)\."
    match = re.search(pattern, url)
    if match:
        filename = match.group(1) + ".html"
    else:
        filename = "webpage.html"

    decision = input("Do you want to store it in a file (y/n): ")
    
    if decision.lower() == "y":
        save_source_code_as_file(source_code, filename)
    
decision=input("Do you want to display it (y/n): ")
if decision.lower()== "y":
	code=extract_source_code(url)
	print(code)
else:
	print(" thank you!! ")
	
        

