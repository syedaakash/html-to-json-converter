from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert_html_to_json', methods=['POST'])
def convert_html_to_json():
    html_directory = 'json'
    for filename in os.listdir(html_directory):
        if filename.endswith('.html'):
            html_file = os.path.join(html_directory, filename)
            convert_html_to_json_single(html_file)
    return jsonify({'status': 'success'})


def convert_html_to_json_single(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    json_string = soup.find('pre').get_text()

    data = json.loads(json_string)

    json_file = os.path.splitext(html_file)[0] + '.json'
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == '__main__':
    app.run(debug=True)
