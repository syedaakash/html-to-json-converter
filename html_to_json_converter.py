from bs4 import BeautifulSoup
import json
import os

html_directory = 'json'

for filename in os.listdir(html_directory):
    if filename.endswith('.html'):
        html_file = os.path.join(html_directory, filename)
        with open(html_file, 'r') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        json_string = soup.find('pre').get_text()

        data = json.loads(json_string)

        json_file = os.path.splitext(html_file)[0] + '.json'
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=2)

print("JSON files have been generated successfully.")
