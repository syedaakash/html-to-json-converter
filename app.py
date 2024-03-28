import json
import os

from flask import Flask, render_template, jsonify, send_from_directory
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/json/<path:filename>')
def serve_json(filename):
    return send_from_directory('json', filename)

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
    pre_tag = soup.find('pre')
    if pre_tag:
        json_string = pre_tag.get_text()

        data = json.loads(json_string)

        json_file = os.path.splitext(html_file)[0] + '.json'
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=2)
    else:
        driver = webdriver.Chrome()
        driver.get(f"http://localhost:5000/{html_file}")

        wait = WebDriverWait(driver, 10)
        dynamic_element = wait.until(EC.visibility_of_element_located((By.ID, "data-div")))

        dynamic_content = dynamic_element.text

        data = json.loads(dynamic_content)

        json_file = os.path.splitext(html_file)[0] + '.json'
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=2)


if __name__ == '__main__':
    app.run(debug=True)
