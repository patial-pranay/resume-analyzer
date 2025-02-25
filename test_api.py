import requests

# Define API endpoint
url = "http://127.0.0.1:5000/upload"

# Open and send a PDF file
with open("your_path_file_here", "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Print response
print(response.json())
